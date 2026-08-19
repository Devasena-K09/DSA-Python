SELECT Email,
       COUNT(*) AS DuplicateCount
FROM Employees
GROUP BY Email
HAVING COUNT(*) > 1;
