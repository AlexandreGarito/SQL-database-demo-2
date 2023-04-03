"""Module for all the interactions with GCP for the project"""

import logging
import os
from google.cloud.sql.connector import Connector
import sqlalchemy
from google.cloud import secretmanager


def get_secret(project_id, secret_name):
    """
    This function connects to the GCP Secret Manager and get the value of a secret.
    The connection is made through a GCP authentication Client allowing for automated
    credentials retrieving with, in this case, either GOOGLE_APPLICATION_CREDENTIALS
    environment variable if run locally or attached service account if run in GCP.

    Args:
        project_id (str): the GCP project ID
        secret_name (str): the secret name inside GCP Secret Manager

    Returns:
        str: The secret value
    """

    client = secretmanager.SecretManagerServiceClient()
    path_secret_name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=path_secret_name)
    secret_value = response.payload.data.decode("UTF-8")
    return secret_value


PROJECT_ID = os.environ["PROJECT_ID"]
SQL_INSTANCE_CONNECTION_NAME1 = get_secret(PROJECT_ID, "SQL_INSTANCE_CONNECTION_NAME1") # same as demo1
SQL_DB_USER1 = get_secret(PROJECT_ID, "SQL_DB_USER1")
SQL_DB_PASS1 = get_secret(PROJECT_ID, "SQL_DB_PASS1")
SQL_DB_NAME2 = get_secret(PROJECT_ID, "SQL_DB_NAME2")


def conn_to_psql():
    """Connects to the GCP Cloud SQL PostgreSQL database"""
    
    
    connector = Connector()

    def getconn_SQL():
        conn = connector.connect(
            SQL_INSTANCE_CONNECTION_NAME1,
            "pg8000",
            user=SQL_DB_USER1,
            password=SQL_DB_PASS1,
            db=SQL_DB_NAME2,
        )
        return conn

    # Create connection pool with 'creator' argument to our connection object
    try:
        pool = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=getconn_SQL,
        )
    except Exception as e:
        logging.warning(f"Connection to GCP database failed!\nThis exception was raised : {e}")
        
    return pool, connector


def close_conn_to_sql(pool, connector):
    """Closes the connection to the GCP Cloud SQL PostgreSQL database"""
    
    connector.close() # Clean up the Connector object only used to authenticate the user
    pool.dispose() # Close the database connections managed by the connection pool
