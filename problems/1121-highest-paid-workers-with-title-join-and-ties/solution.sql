-- your query
SELECT w.name,w.salary,t.title
FROM workers w
JOIN titles t
ON w.title_id=t.title_id
WHERE w.salary in(
    SELECt MAX(salary)
    FROM workers
)
ORDER BY w.name 
