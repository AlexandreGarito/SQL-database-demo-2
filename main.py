""" The main script execute, with an empty database, as follow  :
    - Configure logging
    - Data processing of the selected csv files (cleaning, validation)
    - Connect to the GCP Cloud SQL PostgreSQL database
    - Create the database schema with tables, data constraints, with saved SQL queries
    - Upload data inside each table
    - Query some data to verify that it has been properly inserted
    - Close the connection
"""

import logging
import pandas as pd
from csv_files_data_processing import (
    data_processing_glassdoor_csv, 
    data_processing_glassdoor_overview_competitors_csv,
    data_processing_glassdoor_benefits_comments_csv,
    data_processing_glassdoor_benefits_highlights_csv,
    data_processing_glassdoor_reviews_csv,
    data_processing_glassdoor_salary_salaries_csv,
    data_processing_glassdoor_wwfu_csv,
    data_processing_glassdoor_wwfu_val_captions_csv,
    data_processing_glassdoor_wwfu_val_photos_csv,
    data_processing_glassdoor_wwfu_val_videos_csv
    )
from sql_queries_vars import (
    create_table_glassdoor,
    create_table_glassdoor_oc,
    create_table_glassdoor_bc,
    create_table_glassdoor_bh,
    create_table_glassdoor_r,
    create_table_glassdoor_ss,
    create_table_glassdoor_w,
    create_table_glassdoor_wvc,
    create_table_glassdoor_wvp,
    create_table_glassdoor_wvv,
    query_verify_glassdoor,
    query_verify_bh,
    query_verify_r,
    query_verify_w,
    query_verify_wvv,
    query_verify_wvc,
)
from gcp_interactions import conn_to_psql, close_conn_to_sql

# Logging configuration
logging.basicConfig(
        # filename="logs/app.log",
        handlers=[logging.FileHandler("logs/app.log"), logging.StreamHandler()],
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
logging.info("SCRIPT STARTED")


# Data processing (filtering, cleaning, validating) of 11/15 csv files containing useful data, the other files are not used.
logging.info("Data processing started")
df_glassdoor = data_processing_glassdoor_csv()
logging.info("glassdoor.csv processing done")
df_oc = data_processing_glassdoor_overview_competitors_csv()
logging.info("glassdoor_overview_competitors.csv processing done")
df_bc = data_processing_glassdoor_benefits_comments_csv()
logging.info("glassdoor_benefits_comments.csv processing done")
df_bh = data_processing_glassdoor_benefits_highlights_csv()
logging.info("glassdoor_benefits_highlights.csv processing done")
df_r = data_processing_glassdoor_reviews_csv()
logging.info("glassdoor_reviews.csv processing done")
df_ss = data_processing_glassdoor_salary_salaries_csv()
logging.info("glassdoor_salary_salaries.csv processing done")
df_w = data_processing_glassdoor_wwfu_csv()
logging.info("glassdoor_wwfu.csv processing done")
df_wvc = data_processing_glassdoor_wwfu_val_captions_csv()
logging.info("glassdoor_wwfu_val_captions.csv processing done")
df_wvp = data_processing_glassdoor_wwfu_val_photos_csv()
logging.info("glassdoor_wwfu_val_photos.csv processing done")
df_wvv = data_processing_glassdoor_wwfu_val_videos_csv()
logging.info("glassdoor_wwfu_val_videos.csv processing done")
logging.info("All data processing done")


# Connection to PostgreSQL database in GCP
logging.info("Connecting to GCP database")
pool, connector = conn_to_psql()
logging.info("Connection established")


# Variables containing the SQL queries are initialized in sql_queries_vars.py
# The SQL queries are used to create the database schema, tables & data type constraints, executed in reverse order from 
# outermost to innermost tables to allow foreign keys creation in one step
logging.info("SQL Queries execution started, creating database schema...")
pool.execute(create_table_glassdoor_wvv)  # Table referenced in glassdoor_w
logging.info("Table glassdoor_wwfu_val_videos correctly created")
pool.execute(create_table_glassdoor_wvp)  # Table referenced in glassdoor_w
logging.info("Table glassdoor_wwfu_val_photos correctly created")
pool.execute(create_table_glassdoor_wvc)  # Table referenced in glassdoor_w
logging.info("Table glassdoor_wwfu_val_captions correctly created")
pool.execute(create_table_glassdoor_w)    # Table referenced in glassdoor
logging.info("Table glassdoor_wwfu correctly created")
pool.execute(create_table_glassdoor_ss)   # Table referenced in glassdoor
logging.info("Table glassdoor_salary_salaries correctly created")
pool.execute(create_table_glassdoor_r)    # Table referenced in glassdoor
logging.info("Table glassdoor_reviews correctly created")
pool.execute(create_table_glassdoor_bh)   # Table referenced in glassdoor
logging.info("Table glassdoor_benefits_highlights correctly created")
pool.execute(create_table_glassdoor_bc)   # Table referenced in glassdoor
logging.info("Table glassdoor_benefits_comments correctly created")
pool.execute(create_table_glassdoor_oc)   # Table referenced in glassdoor
logging.info("Table glassdoor_overview_competitors correctly created")
pool.execute(create_table_glassdoor)      # Main table
logging.info("Table glassdoor correctly created")
logging.info("SQL Queries execution done, database schema created")


# Upload data to the database tables in GCP, executed in reverse order from outermost to innermost tables to allow foreign 
# keys creation in one step
logging.info("Uploading data to database")
df_wvc.to_sql("glassdoor_wwfu_val_captions", pool, if_exists="append", index=False)
logging.info("glassdoor_wwfu_val_captions data correctly uploaded")
df_wvp.to_sql("glassdoor_wwfu_val_photos", pool, if_exists="append", index=False)
logging.info("glassdoor_wwfu_val_photos data correctly uploaded")
df_wvv.to_sql("glassdoor_wwfu_val_videos", pool, if_exists="append", index=False)
logging.info("glassdoor_wwfu_val_videos data correctly uploaded")
df_w.to_sql("glassdoor_wwfu", pool, if_exists="append", index=False)
logging.info("glassdoor_wwfu data correctly uploaded")
df_ss.to_sql("glassdoor_salary_salaries", pool, if_exists="append", index=False)
logging.info("glassdoor_salary_salaries data correctly uploaded")
df_r.to_sql("glassdoor_reviews", pool, if_exists="append", index=False)
logging.info("glassdoor_reviews data correctly uploaded")
df_oc.to_sql("glassdoor_overview_competitors", pool, if_exists="append", index=False)
logging.info("glassdoor_overview_competitors data correctly uploaded")
df_bc.to_sql("glassdoor_benefits_comments", pool, if_exists="append", index=False)
logging.info("glassdoor_benefits_comments data correctly uploaded")
df_bh.to_sql("glassdoor_benefits_highlights", pool, if_exists="append", index=False)
logging.info("glassdoor_benefits_highlights data correctly uploaded")
df_glassdoor.to_sql("glassdoor", pool, if_exists="append", index=False)
logging.info("glassdoor data correctly uploaded")
logging.info("All data uploaded to database")

# Verify that all data has been inserted
result_glassdoor = pd.read_sql(query_verify_glassdoor, pool)
result_bh = pd.read_sql(query_verify_bh, pool)
result_r = pd.read_sql(query_verify_r, pool)
result_w = pd.read_sql(query_verify_w, pool)
result_wvv = pd.read_sql(query_verify_wvv, pool)
result_wvc = pd.read_sql(query_verify_wvc, pool)

if (not result_glassdoor.empty and not result_bh.empty and
    not result_r.empty and not result_w.empty and
    not result_wvv.empty and not result_wvc.empty):
    logging.info("Data correctly inserted.")
else :
    logging.info("ERROR : problem with data insertion")
print("SQL query result : \n")
print(f"Result glassdoor:\n{result_glassdoor}\n\n\n\n")
print(f"Result bh:\n{result_bh}\n\n\n\n")
print(f"Result r:\n{result_r}\n\n\n\n")
print(f"Result w:\n{result_w}\n\n\n\n")
print(f"Result wvv:\n{result_wvv}\n\n\n\n")
print(f"Result wvc:\n{result_wvc}\n\n\n\n")


# Close the connection the GCP database
logging.info("Closing connection to database...")
close_conn_to_sql(pool, connector)
logging.info("Connection to database closed.")