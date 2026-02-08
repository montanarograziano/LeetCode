-- Last updated: 08/02/2026, 14:28:15
SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    Activity
WHERE 
    DATEDIFF('2019-07-27', activity_date) < 30 AND DATEDIFF('2019-07-27', activity_date)>=0
GROUP BY 1