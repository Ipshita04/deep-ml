-- your query
SELECT MAX(CASE WHEN rnk=3 THEN salary END) AS nth_salary
FROM(
    SELECT salary,DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employee
)t;