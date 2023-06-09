# SQL Database Setup and Analysis of a Glassdoor Job Listings Dataset

<br>

![illustration pipeline](https://github.com/AlexandreGarito/SQL-database-demo-2/blob/main/images/illustration%20pipeline%20demo-2.png)


### Project summary:  
My objectives for this project were to develop my skills in setting up and interacting with an SQL database, as well as practicing data cleaning, validation, and visualization. For this, I used a Kaggle dataset containing a 2019 web-scraped collection of Glassdoor job listings for data-related positions: https://www.kaggle.com/datasets/andresionek/data-jobs-listings-glassdoor

The dataset, consisting of 15 CSV files with 160,000 records and approximately 1.47 GB of data, contains numerous inconsistencies, missing or invalid entries, and duplicate data, typical of web-scraped datasets. The main CSV file alone has 163 columns and is around 900 MB in size.

My approach involved taking this rather dirty dataset, cleaning and validating it with Python, and then creating a PostgreSQL database in GCP Cloud SQL with an appropriate schema to import the data. I then used SQL queries inside BigQuery to derive insights from the data, which I visualized using GCP Looker (formerly Data Studio).  

Looker dashboard link : https://lookerstudio.google.com/reporting/127231ff-fc3c-464a-a6b5-28d075df9672


<br>

<p align="center">
  <img src="https://github.com/AlexandreGarito/SQL-database-demo-2/blob/main/images/looker1.PNG" width="24.5%" />
  <img src="https://github.com/AlexandreGarito/SQL-database-demo-2/blob/main/images/looker2.PNG" width="24.5%" />
  <img src="https://github.com/AlexandreGarito/SQL-database-demo-2/blob/main/images/looker3.PNG" width="24.5%" />
  <img src="https://github.com/AlexandreGarito/SQL-database-demo-2/blob/main/images/looker4.PNG" width="24.5%" />
</p>



<br>

Tools & skills in this project :

  ✅ Clean and validate a large (1.5GB) and dirty (web-scraped) dataset using Python pandas  
  
  ✅ Design and create a multi-dimensional database schema using SQL  
  
  ✅ Manage compatibility issues involved in the data upload to a PostgreSQL database hosted on GCP  
  
  ✅ Perform SQL-based querying and gain insights using GCP BigQuery  
  
  ✅ Visualize data using GCP Looker (formerly Data Studio)
  
<br>

### Project development overview :

In this project, I chose to work with a dataset that would allow me to practice my data cleaning, database schema design, and data visualization skills. I selected the Glassdoor dataset as it was a good balance between a relatively narrow dataset with a clear theme and sufficient data points to infer some rankings and insights.  

Additionally, the dataset's messy nature, a result of the web scraping process, let me practice my data cleaning skills more thoroughly. The complexity of the dataset (15 files) would mean I could practice my ability to correctly design and build a database schema with a fact table connected to multiple dimensional tables. Also, with a lot of potential fields (200+) to extract insight from, and a size of 1.5GB, working with this dataset enabled me to gain experience with a dataset size and complexity closer to that of a small-scale production database.

The main problems I encountered involved ensuring that the data types and constraints of my pandas DataFrames aligned with those required by the PostgreSQL database. I managed to correctly notice and fix the multiple incompatibilities that prevented the upload by altering the script, and adapting it to the various special cases I encountered. For example, certain foreign key constraints were throwing errors because of inconsistencies in the id fields of some dimensional tables data imported, some records would have NULL or floats values instead of integers.

The main script of the project, main.py, handles everything relating to the data importation and upload to the database: files are imported, filtered, cleaned, validated with Python pandas, then from the empty database the schema is created with Python SQLAlchemy from SQL queries, then the data is uploaded, and then queried to verify that the data has properly been inserted.

To generate the GCP Looker dashboard, I then manually created the particular views I needed in BigQuery, and connected those BigQuery views into GCP Looker in order to create the various elements of the dashboard.

Overall, this project has allowed me to enhance my skills in handling large dirty datasets, cleaning and validating data, as well as extracting valuable insights with SQL in a cloud-based environment.
