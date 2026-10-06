-- your query
SELECT e.id,e.name,e.department,e.salary
FROM employees e
JOIN(
    SELECT department,AVG(salary) AS salary
    FROM employees
    GROUP BY department
)t
ON e.department=t.department AND e.salary>t.salary
ORDER BY e.id
