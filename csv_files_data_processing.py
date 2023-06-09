""" This module stores all the data processing functions for each selected csv file of the dataset, as well some 
utility functions.
"""

import pandas as pd
import numpy as np
import re


def replace_dots(df):
    """Replace dots with underscores in column names for better SQL compatibility in queries"""
    
    df.columns = [col.replace('.', '_') for col in df.columns]
    
    return df


def clean_job_description(text):
    """Removes all the HTML/CSS tags and other random junk from the text, only keeping words"""
    
    if text is None or pd.isna(text):
        return text

    # Remove HTML tags
    text = re.sub("<[^>]+>", "", text)
    text = re.sub("&\w+;|&#\d+;", "", text)
    text = re.sub("[^\w\s]+", " ", text)

    # Convert text to lowercase
    text = text.lower()

    # Remove extra spaces
    text = re.sub("\s+", " ", text)

    # Strip leading/trailing spaces
    text = text.strip()

    return text


def data_processing_glassdoor_csv():
    """Filter, clean and validate the glassdoor.csv file, the main file/table of the dataset."""
    
    df_glassdoor = pd.read_csv("glassdoor_dataset/glassdoor.csv")

    df_glassdoor = replace_dots(df_glassdoor)

    # Filtering the main glassdoor.csv file, a lot of columns are HTML or URL related elements that are not very relevant for our purpose.
    filtered_df_glassdoor = df_glassdoor.loc[
        :,
        [
            "header_easyApply", # Presence of Easy Apply button on job posting
            "header_employerName", # Company's name
            "header_jobTitle", # Job posting title
            "header_posted",  # Date job was posted
            "header_rating",  # Company rating by employees
            "header_urgencyLabel",  # Misleading column name, it actually indicates the presence of the "2019 Glassdoor Best Place to Work" award on the job posting
            "header_payHigh", # Payment at 90th percentile
            "header_payMed", # Payment at 50th percentile
            "header_payLow", # Payment at 10th percentile
            "job_description", # Job description (html)
            "job_jobSource", # Original website origin of job posting
            "map_country",  # do something with country_names_2_digit_codes
            "map_lat",  # Geographical latitude of job posting, 0 for NaN
            "map_lng",  # Geographical longitude of job posting, 0 for NaN
            "map_location", # Location of job posting (variable, city or country), can be different from the company's headquarters
            "overview_foundedYear",  # Year of company's foundation, 0 for NaN
            "overview_hq", # Company's headquarters location
            "overview_industry", # Company's industry, sub-sector
            "overview_revenue", # Company's revenue
            "overview_sector", # Company's sector
            "overview_size", # Company's number of employees bracket
            "overview_stock", # Company's stock
            "overview_type", # Public or private company
            "overview_description", # Company's description
            "overview_mission", # Company's mission
            "overview_competitors",  # id for company's competitor, foreign key to glassdoor_overview_competitors
            "rating_ceo_name", # Company's CEO Name
            "rating_ceoApproval",  # Company's CEO approval rating, <0 or NaN for missing data
            "rating_recommendToFriend",  # Rating from employees for recommendations to friends, <0 or NaN for missing data
            "rating_starRating", # Rating of company from glassdoor users
            "benefits_comments",  # Comments about company's benefits, foreign key to glassdoor_benefits_comments
            "benefits_highlights",  # Highlighted comments & data about company's benefits, foreign key to glassdoor_benefits_highlights
            "reviews",  # Reviews from glassdoor users, foreign key to glassdoor_reviews
            "salary_salaries",  # Data about salaries reported by employees, foreign key to glassdoor_salary_salaries
            "wwfu",  # Data related to company's mission, foreign key to glassdoor_wwfu
        ],
    ]


    # Transform columns with floats having zero decimal value into integers
    columns_to_int = [
        "header_payHigh",
        "header_payMed",
        "header_payLow",
        "overview_foundedYear",
        "overview_competitors",
        "benefits_comments",
        "benefits_highlights",
        "wwfu",
    ]
    for column in columns_to_int:
        filtered_df_glassdoor[column] = filtered_df_glassdoor[column].astype(pd.Int64Dtype())


    # Replace negative values with NaN
    columns_to_replace_neg = [
        "header_rating",
        "rating_starRating",
        "rating_ceoApproval",
        "rating_recommendToFriend",
    ]
    for column in columns_to_replace_neg:
        filtered_df_glassdoor[column] = filtered_df_glassdoor[column].apply(lambda x: np.nan if x < 0 else x)

    # Replace zero values with NaN
    columns_to_replace_zero = [
        "map_lat",
        "map_lng",
    ]
    for column in columns_to_replace_zero:
        filtered_df_glassdoor[column] = filtered_df_glassdoor[column].apply(lambda x: np.nan if x == 0 else x)

    # Replace outlier/erroneous low salaries values with NaN
    columns_to_replace_outlier_salaries = [
        "header_payHigh",
        "header_payMed",
        "header_payLow",
        "salary_salaries",
    ]
    for column in columns_to_replace_outlier_salaries:
        filtered_df_glassdoor[column] = filtered_df_glassdoor[column].apply(lambda x: np.nan if pd.isna(x) or x < 10000 else x)

    # Replace outlier/erroneous years values with NaN
    columns_to_replace_outlier_years = [
        "overview_foundedYear",
    ]
    for column in columns_to_replace_outlier_years:
        filtered_df_glassdoor[column] = filtered_df_glassdoor[column].apply(lambda x: np.nan if x < 1000 else x)

    # Remove only rows with all missing values
    filtered_df_glassdoor.dropna(how="all", inplace=True)

    # Remove duplicates
    filtered_df_glassdoor.drop_duplicates(inplace=True)

    # Removes all the HTML/CSS tags and other random junk from the text, only keeping words
    filtered_df_glassdoor["job_description"] = filtered_df_glassdoor["job_description"].apply(clean_job_description)

    # Discrepancies between the use of camelCase for some df columns names and PostgreSQL autoconverting all of 
    # them to lowercase automatically would cause errors when uploading, so we convert everything to lowercase.
    filtered_df_glassdoor = filtered_df_glassdoor.rename(columns=lambda x: x.lower())

    """ #FIME: DEBUGGING LENGTH CUT
    new_length = len(filtered_df_glassdoor) // 100
    filtered_df_glassdoor = filtered_df_glassdoor.iloc[:new_length] """

    return filtered_df_glassdoor


def data_processing_glassdoor_overview_competitors_csv():
    """Clean and validate the glassdoor_overview_competitors.csv file."""
    
    df_oc = pd.read_csv("glassdoor_dataset/glassdoor_overview_competitors.csv")

    df_oc = replace_dots(df_oc)
    
    df_oc = df_oc.drop_duplicates(subset='id', keep='first')
    
    # Discrepancies between the use of camelCase for some df columns names and PostgreSQL autoconverting all of 
    # them to lowercase automatically would cause errors when uploading, so we convert everything to lowercase.
    df_oc = df_oc.rename(columns=lambda x: x.lower())
    
    """ #FIME: DEBUGGING LENGTH CUT
    new_length = len(df_oc) // 100
    df_oc = df_oc.iloc[:new_length] """
    
    return df_oc


def data_processing_glassdoor_benefits_comments_csv():
    """Clean and validate the glassdoor_benefits_comments.csv file."""

    df_bc = pd.read_csv("glassdoor_dataset/glassdoor_benefits_comments.csv")

    df_bc = replace_dots(df_bc)
    
    df_bc = df_bc.drop_duplicates(subset='id', keep='first')
    

    # Transform floats with zero decimal values to integers
    columns_to_int = [
        "index",
        "benefits_comments_val_rating",
    ]
    for column in columns_to_int:
        df_bc[column] = df_bc[column].astype(pd.Int64Dtype())
    
    # Discrepancies between the use of camelCase for some df columns names and PostgreSQL autoconverting all of 
    # them to lowercase automatically would cause errors when uploading, so we convert everything to lowercase.
    df_bc = df_bc.rename(columns=lambda x: x.lower())
    
    """ #FIME: DEBUGGING LENGTH CUT
    new_length = len(df_bc) // 100
    df_bc = df_bc.iloc[:new_length] """
    
    return df_bc


def data_processing_glassdoor_benefits_highlights_csv():
    """Clean and validate the glassdoor_benefits_highlights.csv file."""

    df_bh = pd.read_csv("glassdoor_dataset/glassdoor_benefits_highlights.csv")

    df_bh = replace_dots(df_bh)
    
    df_bh = df_bh.drop_duplicates(subset='id', keep='first')
    
    # Transform floats with zero decimal values to integers
    columns_to_int = [
        "index",
        "benefits_highlights_val_commentCount",
    ]
    for column in columns_to_int:
        df_bh[column] = df_bh[column].astype(pd.Int64Dtype())

    # Discrepancies between the use of camelCase for some df columns names and PostgreSQL autoconverting all of 
    # them to lowercase automatically would cause errors when uploading, so we convert everything to lowercase.
    df_bh = df_bh.rename(columns=lambda x: x.lower())

    """ #FIME: DEBUGGING LENGTH CUT
    new_length = len(df_bh) // 100
    df_bh = df_bh.iloc[:new_length] """
    
    return df_bh


def data_processing_glassdoor_reviews_csv():
    """Clean and validate the glassdoor_reviews.csv file."""

    df_r = pd.read_csv("glassdoor_dataset/glassdoor_reviews.csv")

    df_r = replace_dots(df_r)
    
    df_r = df_r.drop_duplicates(subset='id', keep='first')
    

    # Transform floats with zero decimal values to integers
    # I found that in some columns, some rare values actually contain decimals (3.5/5 rating for example), I chose to keep those columns as floats
    columns_to_int = [
        "index",
        "reviews_val_helpfulCount",
        "reviews_val_id",
        # "reviews_val_reviewRatings_careerOpportunities", # Some rare decimals are hidden in this column, keeping as floats
        # "reviews_val_reviewRatings_compBenefits",  # Some decimals are hidden in this column, keeping as floats
        "reviews_val_reviewRatings_cultureValues",
        "reviews_val_reviewRatings_overall", 
        # "reviews_val_reviewRatings_seniorManagement",  # Some decimals are hidden in this column, keeping as floats
        # "reviews_val_reviewRatings_worklifeBalance",  # Some decimals are hidden in this column, keeping as floats
        "reviews_val_summaryPoints_ceoApproval",
        "reviews_val_summaryPoints_outlook",
        "reviews_val_summaryPoints_recommend",
        "reviews_val_reviewResponses",
    ]
    for column in columns_to_int:
        df_r[column] = df_r[column].astype(pd.Int64Dtype())

    # Discrepancies between the use of camelCase for some df columns names and PostgreSQL autoconverting all of 
    # them to lowercase automatically would cause errors when uploading, so we convert everything to lowercase.
    df_r = df_r.rename(columns=lambda x: x.lower())

    temp_value = -1
    df_r['reviews_val_reviewresponses'].fillna(temp_value, inplace=True)

    """ #FIME: DEBUGGING LENGTH CUT
    new_length = len(df_r) // 100
    df_r = df_r.iloc[:new_length] """
    
    return df_r


def data_processing_glassdoor_salary_salaries_csv():
    """Clean and validate the glassdoor_salary_salaries.csv file."""

    df_ss = pd.read_csv("glassdoor_dataset/glassdoor_salary_salaries.csv")

    df_ss = replace_dots(df_ss)

    df_ss = df_ss.drop_duplicates(subset='id', keep='first')
    
    # Transform floats with zero decimal values to integers
    columns_to_int = [
        "index",
        "salary_salaries_val_basePayCount",
    ]
    for column in columns_to_int:
        df_ss[column] = df_ss[column].astype(pd.Int64Dtype())
    
    # Discrepancies between the use of camelCase for some df columns names and PostgreSQL autoconverting all of 
    # them to lowercase automatically would cause errors when uploading, so we convert everything to lowercase.
    df_ss = df_ss.rename(columns=lambda x: x.lower())
    
    """ #FIME: DEBUGGING LENGTH CUT
    new_length = len(df_ss) // 100
    df_ss = df_ss.iloc[:new_length] """
    
    return df_ss


def data_processing_glassdoor_wwfu_csv():
    """Clean and validate the glassdoor_wwfu.csv file."""

    df_w = pd.read_csv("glassdoor_dataset/glassdoor_wwfu.csv")

    df_w = replace_dots(df_w)
    
    df_w = df_w.drop_duplicates(subset='id', keep='first')
    

    # Transform floats with zero decimal values to integers
    columns_to_int = [
        "wwfu_val_videos",
        "wwfu_val_photos",
        "wwfu_val_captions",
    ]
    for column in columns_to_int:
        df_w[column] = df_w[column].astype(pd.Int64Dtype())

    # Cleaning HTML/CSS tags
    df_w["wwfu_val_body"] = df_w["wwfu_val_body"].apply(clean_job_description)

    # Discrepancies between the use of camelCase for some df columns names and PostgreSQL autoconverting all of 
    # them to lowercase automatically would cause errors when uploading, so we convert everything to lowercase.
    df_w = df_w.rename(columns=lambda x: x.lower())

    
    """ #FIME: DEBUGGING LENGTH CUT
    new_length = len(df_w) // 100
    df_w = df_w.iloc[:new_length] """
    
    return df_w


def data_processing_glassdoor_wwfu_val_captions_csv():
    """Clean and validate the glassdoor_wwfu_val_captions.csv file."""

    df_wvc = pd.read_csv("glassdoor_dataset/glassdoor_wwfu_val_captions.csv")
    
    df_wvc = replace_dots(df_wvc)
    
    df_wvc = df_wvc.drop_duplicates(subset='id', keep='first')
    
    # Discrepancies between the use of camelCase for some df columns names and PostgreSQL autoconverting all of 
    # them to lowercase automatically would cause errors when uploading, so we convert everything to lowercase.
    df_wvc = df_wvc.rename(columns=lambda x: x.lower())
    
    """ #FIME: DEBUGGING LENGTH CUT
    new_length = len(df_wvc) // 100
    df_wvc = df_wvc.iloc[:new_length] """
    
    return df_wvc


def data_processing_glassdoor_wwfu_val_photos_csv():
    """Clean and validate the glassdoor_wwfu_val_photos.csv file."""

    df_wvp = pd.read_csv("glassdoor_dataset/glassdoor_wwfu_val_photos.csv")
    
    df_wvp = replace_dots(df_wvp)
    
    df_wvp = df_wvp.drop_duplicates(subset='id', keep='first')

    # Discrepancies between the use of camelCase for some df columns names and PostgreSQL autoconverting all of 
    # them to lowercase automatically would cause errors when uploading, so we convert everything to lowercase.
    df_wvp = df_wvp.rename(columns=lambda x: x.lower())

    """ #FIME: DEBUGGING LENGTH CUT
    new_length = len(df_wvp) // 100
    df_wvp = df_wvp.iloc[:new_length] """

    return df_wvp


def data_processing_glassdoor_wwfu_val_videos_csv():
    """Clean and validate the glassdoor_wwfu_val_videos.csv file."""    

    df_wvv = pd.read_csv("glassdoor_dataset/glassdoor_wwfu_val_videos.csv")
    
    df_wvv = replace_dots(df_wvv)
    
    # Certain id duplicates would cause errors when uploading
    df_wvv = df_wvv.drop_duplicates(subset='id', keep='first')
    
    # Discrepancies between the use of camelCase for some df columns names and PostgreSQL autoconverting all of 
    # them to lowercase automatically would cause errors when uploading, so we convert everything to lowercase.
    df_wvv = df_wvv.rename(columns=lambda x: x.lower())
    
    """ #FIME: DEBUGGING LENGTH CUT
    new_length = len(df_wvv) // 100
    df_wvv = df_wvv.iloc[:new_length] """
    
    return df_wvv

