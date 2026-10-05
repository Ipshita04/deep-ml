-- your query
SELECT user_id,MIN(login_date) AS first_login
FROM logins
WHERE user_id IN(
    SELECT l1.user_id
    FROM logins l1
    JOIN logins l2
    ON l1.user_id=l2.user_id AND l2.login_date=l1.login_date+INTERVAL '1day'    
)
GROUP BY user_id
ORDER BY user_id;