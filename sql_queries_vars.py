""" This module stores all the SQL queries related to the main script.
    Those queries can be quite long so they are put here to save viewing space elsewhere and facilitate code readability.
"""




create_table_glassdoor = '''
    CREATE TABLE glassdoor (
        id SERIAL PRIMARY KEY,
        header_easyapply BOOLEAN,
        header_employername VARCHAR,
        header_jobtitle VARCHAR,
        header_posted VARCHAR,
        header_rating FLOAT,
        header_urgencylabel VARCHAR,
        header_payhigh INTEGER,
        header_paymed INTEGER,
        header_paylow INTEGER,
        job_description VARCHAR,
        job_jobsource VARCHAR,
        map_country VARCHAR,
        map_lat FLOAT,
        map_lng FLOAT,
        map_location VARCHAR,
        overview_foundedYear INTEGER,
        overview_hq VARCHAR,
        overview_industry VARCHAR,
        overview_revenue VARCHAR,
        overview_sector VARCHAR,
        overview_size VARCHAR,
        overview_stock VARCHAR,
        overview_type VARCHAR,
        overview_description VARCHAR,
        overview_mission VARCHAR,
        overview_competitors INTEGER,
        rating_ceo_name VARCHAR,
        rating_ceoapproval FLOAT,
        rating_recommendtofriend FLOAT,
        rating_starrating FLOAT,
        benefits_comments INTEGER,
        benefits_highlights INTEGER,
        reviews INTEGER,
        salary_salaries INTEGER,
        wwfu INTEGER,
        FOREIGN KEY (overview_competitors) REFERENCES glassdoor_overview_competitors(id),
        FOREIGN KEY (benefits_comments) REFERENCES glassdoor_benefits_comments(id),
        FOREIGN KEY (benefits_highlights) REFERENCES glassdoor_benefits_highlights(id),
        FOREIGN KEY (reviews) REFERENCES glassdoor_reviews(id),
        FOREIGN KEY (salary_salaries) REFERENCES glassdoor_salary_salaries(id),
        FOREIGN KEY (wwfu) REFERENCES glassdoor_wwfu(id)
    );
    '''



create_table_glassdoor_oc = '''
    CREATE TABLE glassdoor_overview_competitors (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        overview_competitors_val VARCHAR
    );
    '''



create_table_glassdoor_bc = '''
    CREATE TABLE glassdoor_benefits_comments (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        benefits_comments_val_city VARCHAR,
        benefits_comments_val_comment VARCHAR,
        benefits_comments_val_createdate VARCHAR,
        benefits_comments_val_currentjob VARCHAR,
        benefits_comments_val_jobtitle VARCHAR,
        benefits_comments_val_rating INTEGER,
        benefits_comments_val_state VARCHAR
    );
    '''



create_table_glassdoor_bh = '''
    CREATE TABLE glassdoor_benefits_highlights (
        id INTEGER PRIMARY KEY,
        benefits_highlights_val_highlightphrase VARCHAR,
        benefits_highlights_val_icon VARCHAR,
        benefits_highlights_val_name VARCHAR,
        index INTEGER,
        benefits_highlights_val_commentcount INTEGER
    );
    '''



create_table_glassdoor_r = '''
    CREATE TABLE glassdoor_reviews (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        reviews_val_cons VARCHAR,
        reviews_val_date VARCHAR,
        reviews_val_featured VARCHAR,
        reviews_val_helpfulcount INTEGER,
        reviews_val_id INTEGER,
        reviews_val_pros VARCHAR,
        reviews_val_publishedon VARCHAR,
        reviews_val_publisher VARCHAR,
        reviews_val_reviewratings_careeropportunities FLOAT,
        reviews_val_reviewratings_compbenefits FLOAT,
        reviews_val_reviewratings_culturevalues INTEGER,
        reviews_val_reviewratings_overall INTEGER,
        reviews_val_reviewratings_seniormanagement FLOAT,
        reviews_val_reviewratings_worklifebalance FLOAT,
        reviews_val_reviewerduration VARCHAR,
        reviews_val_reviewerinformation VARCHAR,
        reviews_val_reviewerjobtitle VARCHAR,
        reviews_val_reviewerlocation VARCHAR,
        reviews_val_reviewerstatus VARCHAR,
        reviews_val_summarypoints_ceoapproval INTEGER,
        reviews_val_summarypoints_outlook INTEGER,
        reviews_val_summarypoints_recommend INTEGER,
        reviews_val_title VARCHAR,
        reviews_val_advicetomanagement VARCHAR,
        reviews_val_companyresponse VARCHAR,
        reviews_val_reviewresponses INTEGER
    );
    '''



create_table_glassdoor_ss = '''
CREATE TABLE glassdoor_salary_salaries (
    id INTEGER PRIMARY KEY,
    index INTEGER,
    salary_salaries_val_basepaycount INTEGER,
    salary_salaries_val_jobtitle VARCHAR,
    salary_salaries_val_payperiod VARCHAR,
    salary_salaries_val_salarypercentilemap_paypercentile10 FLOAT,
    salary_salaries_val_salarypercentilemap_paypercentile90 FLOAT,
    salary_salaries_val_salarypercentilemap_paypercentile50 FLOAT,
    salary_salaries_val_salarytype VARCHAR
);
'''


create_table_glassdoor_w = '''
    CREATE TABLE glassdoor_wwfu (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        wwfu_val_body VARCHAR,
        wwfu_val_id INTEGER,
        wwfu_val_title VARCHAR,
        wwfu_val_type VARCHAR,
        wwfu_val_videos INTEGER,
        wwfu_val_photos INTEGER,
        wwfu_val_captions INTEGER,
        FOREIGN KEY (wwfu_val_videos) REFERENCES glassdoor_wwfu_val_videos(id),
        FOREIGN KEY (wwfu_val_photos) REFERENCES glassdoor_wwfu_val_photos(id),
        FOREIGN KEY (wwfu_val_captions) REFERENCES glassdoor_wwfu_val_captions(id)
    );
    '''



create_table_glassdoor_wvc = '''
    CREATE TABLE glassdoor_wwfu_val_captions (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        wwfu_val_captions_val VARCHAR
    );
    '''



create_table_glassdoor_wvp = '''
    CREATE TABLE glassdoor_wwfu_val_photos (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        wwfu_val_photos_val VARCHAR
    );
    '''



create_table_glassdoor_wvv = '''
    CREATE TABLE glassdoor_wwfu_val_videos (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        wwfu_val_videos_val VARCHAR
    );
    '''


query_verify_glassdoor = """
SELECT * FROM glassdoor
LIMIT 10;
"""


query_verify_bh = """
SELECT * FROM glassdoor_benefits_highlights
LIMIT 10;
"""


query_verify_r = """
SELECT * FROM glassdoor_reviews
LIMIT 10;
"""


query_verify_w = """
SELECT * FROM glassdoor_wwfu
LIMIT 10;
"""


query_verify_wvv = """
SELECT * FROM glassdoor_wwfu_val_videos
LIMIT 10;
"""


query_verify_wvc = """
SELECT * FROM glassdoor_wwfu_val_captions
LIMIT 10;
"""
