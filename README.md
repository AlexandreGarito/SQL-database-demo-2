# SQL database set-up & querying Glassdoor dataset (⚠ work in progress ⚠) :

### Project summary:  
In order to train my ability to set up and interact with an SQL database, I found a dataset on Kaggle containing a 2019 web-scraped collection of Glassdoor job listings for data-related positions: https://www.kaggle.com/datasets/andresionek/data-jobs-listings-glassdoor  
The dataset contains 15 CSV files, totaling 160,000 records and approximately 1.47 GB of data. The main CSV file consists of 160 columns and is around 900 MB in size. As expected from a web-scraped dataset, it suffers from many inconsistencies, missing or invalid entries, and duplicate data.

My objective was to take this rather untidy dataset, clean it, validate it, then create a PostgreSQL database in GCP Cloud SQL with an appropriate database schema to properly receive the imported data and ensure data integrity within the database. Finally, I'd use BigQuery to extract some analysis and insights, which will then be visualized in GCP Data Studio.


Goals achieved with this project :  

  ✅ Cleaning & validating a rather large (1.5GB) and dirty (webscraped) dataset with pandas  
  ✅ Database schema creation with SQL (11 tables)  
  ✅ Managing a complex data upload to a PostgreSQL database hosted in GCP  
  ⬜ SQL based analysis with GCP BigQuery  
  ⬜ Vizualisation with GCP Data Studio  
  
### Project development overview :


