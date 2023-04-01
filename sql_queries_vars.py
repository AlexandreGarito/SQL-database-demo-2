




create_table_glassdoor = '''
    CREATE TABLE glassdoor (
        id SERIAL PRIMARY KEY,
        gaTrackerData_jobTitle VARCHAR,
        gaTrackerData_location VARCHAR,
        gaTrackerData_locationType VARCHAR,
        gaTrackerData_sector VARCHAR,
        header_easyApply BOOLEAN,
        header_employerName VARCHAR,
        header_jobTitle VARCHAR,
        header_location VARCHAR,
        header_posted VARCHAR,
        header_rating REAL,
        header_urgencyLabel VARCHAR,
        header_payHigh INTEGER,
        header_payMed INTEGER,
        header_payLow INTEGER,
        job_description VARCHAR,
        job_jobSource VARCHAR,
        map_country VARCHAR,
        map_employerName VARCHAR,
        map_lat REAL,
        map_lng REAL,
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
        rating_ceoApproval REAL,
        rating_recommendToFriend REAL,
        rating_starRating REAL,
        benefits_comments INTEGER,
        benefits_highlights INTEGER,
        reviews INTEGER,
        salary_salaries REAL,
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
        benefits_comments_val_createDate VARCHAR,
        benefits_comments_val_currentJob VARCHAR,
        benefits_comments_val_jobTitle VARCHAR,
        benefits_comments_val_rating INTEGER,
        benefits_comments_val_state VARCHAR
    );
    '''



create_table_glassdoor_bh = '''
    CREATE TABLE glassdoor_benefits_highlights (
        id INTEGER PRIMARY KEY,
        benefits_highlights_val_highlightPhrase VARCHAR,
        benefits_highlights_val_icon VARCHAR,
        benefits_highlights_val_name VARCHAR,
        index INTEGER,
        benefits_highlights_val_commentCount INTEGER
    );
    '''



create_table_glassdoor_r = '''
    CREATE TABLE glassdoor_reviews (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        reviews_val_cons VARCHAR,
        reviews_val_date VARCHAR,
        reviews_val_featured VARCHAR,
        reviews_val_helpfulCount INTEGER,
        reviews_val_id INTEGER,
        reviews_val_pros VARCHAR,
        reviews_val_publishedOn VARCHAR,
        reviews_val_publisher VARCHAR,
        reviews_val_reviewRatings_careerOpportunities REAL,
        reviews_val_reviewRatings_compBenefits REAL,
        reviews_val_reviewRatings_cultureValues INTEGER,
        reviews_val_reviewRatings_overall INTEGER,
        reviews_val_reviewRatings_seniorManagement REAL,
        reviews_val_reviewRatings_worklifeBalance REAL,
        reviews_val_reviewerDuration VARCHAR,
        reviews_val_reviewerInformation VARCHAR,
        reviews_val_reviewerJobTitle VARCHAR,
        reviews_val_reviewerLocation VARCHAR,
        reviews_val_reviewerStatus VARCHAR,
        reviews_val_summaryPoints_ceoApproval INTEGER,
        reviews_val_summaryPoints_outlook INTEGER,
        reviews_val_summaryPoints_recommend INTEGER,
        reviews_val_title VARCHAR,
        reviews_val_adviceToManagement VARCHAR,
        reviews_val_companyResponse VARCHAR,
        reviews_val_reviewResponses INTEGER
    );
    '''



create_table_glassdoor_rvr = '''
    CREATE TABLE glassdoor_reviews_val_reviewResponses (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        reviews_val_reviewResponses_val_createDate VARCHAR,
        reviews_val_reviewResponses_val_helpfulCount INTEGER,
        reviews_val_reviewResponses_val_jobTitle VARCHAR,
        reviews_val_reviewResponses_val_notHelpfulCount INTEGER,
        reviews_val_reviewResponses_val_responseText VARCHAR,
        reviews_val_reviewResponses_val_responseTextLength INTEGER,
        reviews_val_reviewResponses_val_totalHelpfulCount INTEGER,
        reviews_val_reviewResponses_val_updateDate VARCHAR
    );
    '''



create_table_glassdoor_ss = '''
CREATE TABLE glassdoor_salary_salaries (
    id INTEGER PRIMARY KEY,
    index INTEGER,
    salary_salaries_val_basePayCount INTEGER,
    salary_salaries_val_jobTitle VARCHAR,
    salary_salaries_val_payPeriod VARCHAR,
    salary_salaries_val_salaryPercentileMap_payPercentile10 REAL,
    salary_salaries_val_salaryPercentileMap_payPercentile90 REAL,
    salary_salaries_val_salaryPercentileMap_payPercentile50 REAL,
    salary_salaries_val_salaryType VARCHAR
);
'''


create_table_glassdoor_w = '''
    CREATE TABLE glassdoor_wwfu (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        wwf_val_body VARCHAR,
        wwf_val_id INTEGER,
        wwf_val_title VARCHAR,
        wwf_val_type VARCHAR,
        FOREIGN KEY (wwf_val_videos) INTEGER,
        wwf_val_photos INTEGER,
        wwf_val_captions INTEGER
    );
    '''



create_table_glassdoor_wvc = '''
    CREATE TABLE glassdoor_wwfu_val_captions (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        wwfuf_val_captions_val VARCHAR
    );
    '''



create_table_glassdoor_wvp = '''
    CREATE TABLE glassdoor_wwfu_val_photos (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        wwfuf_val_photos_val VARCHAR
    );
    '''



create_table_glassdoor_wvv = '''
    CREATE TABLE glassdoor_wwfu_val_videos (
        id INTEGER PRIMARY KEY,
        index INTEGER,
        wwfuf_val_videos_val VARCHAR
    );
    '''