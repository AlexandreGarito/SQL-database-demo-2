/*
This SQL file contains the queries used inside BigQuery that were linked to the Looker Dashboard. 

These queries are not used in the main.py script. 

To ensure security, the original connection ID was replaced with a "CONNECTION_ID" placeholder.
The salaries originally in British pounds have been converted to US dollars using the GBP/USD exchange rate (0.78154) on 
the day the dataset was webscrapped.
*/


-- Job Postings Count by Title
SELECT 
    header_jobtitle, 
    COUNT(header_jobtitle) AS count
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT header_jobtitle FROM glassdoor;")
GROUP BY 
    header_jobtitle 
ORDER BY 
    count DESC;


-- Job Postings Count by Location
SELECT 
    map_location, 
    COUNT(*) AS job_count
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
WHERE 
    map_location != ''
GROUP BY 
    map_location 
ORDER BY 
    job_count DESC;


-- Job Postings Count by Industry
SELECT 
    overview_industry, 
    COUNT(*) AS job_count
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
WHERE 
    overview_industry != ''
GROUP BY 
    overview_industry 
ORDER BY 
    job_count DESC;


-- Geographical Location (Map) of Data-Related Jobs
SELECT 
    map_location, 
    map_lat, 
    map_lng, 
    COUNT(*) AS job_count
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
GROUP BY 
    map_location, 
    map_lat, 
    map_lng 
ORDER BY 
    job_count DESC;


-- Best median salary by city
SELECT 
    map_location, 
    COUNT(*) AS job_count, 
    AVG(header_paymed) AS avg_pay_med
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
WHERE 
    map_location != ''
GROUP BY 
    map_location
HAVING 
    job_count > 20
ORDER BY 
    avg_pay_med DESC 
LIMIT 100;


-- Best cities by highest number of job posting company ratings above 4.0 
SELECT 
    map_location, 
    COUNT(*) AS job_count, 
    AVG(header_rating) AS avg_rating
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
WHERE 
    map_location != '' 
    AND header_rating >= 4
GROUP BY 
    map_location
HAVING 
    job_count > 50
ORDER BY 
    job_count DESC 
LIMIT 100;


-- Best small cities by average company ratings
SELECT 
    map_location, 
    COUNT(*) AS job_count, 
    AVG(header_rating) AS avg_rating, 
    AVG(rating_recommendtofriend) AS avg_recommend_to_friend, 
    COUNT(header_urgencylabel) AS best_workplaces_awards, 
    AVG(rating_starrating) AS avg_star_rating
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
WHERE 
    map_location != ''
GROUP BY 
    map_location
HAVING 
    job_count > 150
ORDER BY 
    avg_rating DESC, 
    avg_recommend_to_friend DESC, 
    best_workplaces_awards DESC, 
    avg_star_rating DESC
LIMIT 50;


-- Best big cities by average company ratings
SELECT 
    map_location,
    COUNT(*) AS job_count,
    AVG(header_rating) AS avg_rating,
    AVG(rating_recommendtofriend) AS avg_recommend_to_friend,
    COUNT(header_urgencylabel) AS best_workplaces_awards,
    AVG(rating_starrating) AS avg_star_rating
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
WHERE 
    map_location != ''
GROUP BY 
    map_location
HAVING 
    job_count > 1500
ORDER BY 
    avg_rating DESC,
    avg_recommend_to_friend DESC, 
    best_workplaces_awards DESC, 
    avg_star_rating DESC
LIMIT 50;


-- Best industries by average pay, job postings and ratings, ordered by average pay by default
SELECT 
    overview_industry,
    COUNT(*) AS job_count,
    ROUND(AVG(header_paymed) / 0.7815448626756474) AS avg_salary_usd,
    ROUND(AVG(header_rating), 1) AS avg_rating
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
WHERE 
    overview_industry != ''
GROUP BY 
    overview_industry
HAVING 
    COUNT(*) > 200
ORDER BY 
    avg_salary_usd DESC;


-- Small companies by average rating, median pay and job count, ordered by default by median pay
SELECT 
    header_employername,
    overview_hq,
    overview_revenue,
    COUNT(*) AS job_count,
    ROUND(AVG(header_paymed)/0.7815448626756474) AS avg_salary_usd,
    ROUND(AVG(header_rating), 1) AS avg_rating
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
WHERE 
    header_employername != ''
GROUP BY 
    header_employername,
    overview_hq,
    overview_revenue
HAVING 
    COUNT(*) > 5
ORDER BY 
    avg_salary_usd DESC;


-- Big companies by average rating, median pay and job count, ordered by default by median pay
SELECT 
    header_employername,
    overview_hq,
    overview_revenue,
    COUNT(*) AS job_count,
    ROUND(AVG(header_paymed)/0.7815448626756474) AS avg_salary_usd,
    ROUND(AVG(header_rating), 1) AS avg_rating
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
WHERE 
    header_employername != ''
GROUP BY 
    header_employername,
    overview_hq,
    overview_revenue
HAVING 
    COUNT(*) > 200
ORDER BY 
    avg_salary_usd DESC;


-- Best Median Salary by Company Revenue Bracket
SELECT 
    overview_revenue,
    AVG(header_paymed) AS avg_salary
FROM 
    EXTERNAL_QUERY("CONNECTION_ID", "SELECT * FROM glassdoor;")
WHERE 
    header_jobtitle != ''
    AND overview_revenue != ''
GROUP BY 
    overview_revenue
ORDER BY 
    avg_salary DESC;






