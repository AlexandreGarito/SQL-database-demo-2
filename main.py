import logging
from csv_files_data_processing import (
    data_processing_glassdoor_csv, 
    data_processing_glassdoor_overview_competitors_csv,
    data_processing_glassdoor_benefits_comments_csv,
    data_processing_glassdoor_benefits_highlights_csv,
    data_processing_glassdoor_reviews_csv,
    data_processing_glassdoor_reviews_val_reviewResponses_csv,
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
    create_table_glassdoor_rvr,
    create_table_glassdoor_ss,
    create_table_glassdoor_w,
    create_table_glassdoor_wvc,
    create_table_glassdoor_wvp,
    create_table_glassdoor_wvv,
)
from gcp_interactions import conn_to_psql, close_conn_to_sql

logging.basicConfig(
        # filename="logs/app.log",
        handlers=[logging.FileHandler("logs/app.log"), logging.StreamHandler()],
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
logging.info("SCRIPT STARTED")

# Data processing (filtering, cleaning, validating) of 11/15 csv files containing useful data, the other files are not used.
logging.info("Data processing started")
logging.info("glassdoor.csv processing started")

df_glassdoor = data_processing_glassdoor_csv()
logging.info("glassdoor.csv processing done")

logging.info("Processing the other files...")
df_oc = data_processing_glassdoor_overview_competitors_csv()
df_bc = data_processing_glassdoor_benefits_comments_csv()
df_bh = data_processing_glassdoor_benefits_highlights_csv()
df_r = data_processing_glassdoor_reviews_csv()
df_rvr = data_processing_glassdoor_reviews_val_reviewResponses_csv()
df_ss = data_processing_glassdoor_salary_salaries_csv()
df_w = data_processing_glassdoor_wwfu_csv()
df_wvc = data_processing_glassdoor_wwfu_val_captions_csv()
df_wvp = data_processing_glassdoor_wwfu_val_photos_csv()
df_wvv = data_processing_glassdoor_wwfu_val_videos_csv()
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
pool.execute(create_table_glassdoor_wvp)  # Table referenced in glassdoor_w
pool.execute(create_table_glassdoor_wvc)  # Table referenced in glassdoor_w
pool.execute(create_table_glassdoor_w)    # Table referenced in glassdoor
pool.execute(create_table_glassdoor_ss)   # Table referenced in glassdoor
pool.execute(create_table_glassdoor_rvr)  # Table referenced in glassdoor_r
pool.execute(create_table_glassdoor_r)    # Table referenced in glassdoor
pool.execute(create_table_glassdoor_bh)   # Table referenced in glassdoor
pool.execute(create_table_glassdoor_bc)   # Table referenced in glassdoor
pool.execute(create_table_glassdoor_oc)   # Table referenced in glassdoor
pool.execute(create_table_glassdoor)      # Main table
logging.info("SQL Queries execution done, database schema created")


# Upload data to the database tables in GCP, executed in reverse order from outermost to innermost tables to allow foreign 
# keys creation in one step
logging.info("Uploading data to database")
df_wvc.to_sql("glassdoor_wwfu_val_captions", pool, if_exists="replace", index=False)
df_wvp.to_sql("glassdoor_wwfu_val_photos", pool, if_exists="replace", index=False)
df_wvv.to_sql("glassdoor_wwfu_val_videos", pool, if_exists="replace", index=False)
df_w.to_sql("glassdoor_wwfu", pool, if_exists="replace", index=False)
df_ss.to_sql("glassdoor_salary_salaries", pool, if_exists="replace", index=False)
df_rvr.to_sql("glassdoor_reviews_val_reviewResponses", pool, if_exists="replace", index=False)
df_r.to_sql("glassdoor_reviews", pool, if_exists="replace", index=False)
df_oc.to_sql("glassdoor_overview_competitors", pool, if_exists="replace", index=False)
df_bc.to_sql("glassdoor_benefits_comments", pool, if_exists="replace", index=False)
df_bh.to_sql("glassdoor_benefits_highlights", pool, if_exists="replace", index=False)
df_glassdoor.to_sql("glassdoor", pool, if_exists="replace", index=False)
logging.info("Data upload to database done")


# Close the connection the GCP database
close_conn_to_sql(pool, connector)