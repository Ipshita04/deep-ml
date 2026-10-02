-- Employee name + department name
SELECT e.name, d.name AS department
FROM employees e
LEFT JOIN departments d 
ON e.department_id=d.id