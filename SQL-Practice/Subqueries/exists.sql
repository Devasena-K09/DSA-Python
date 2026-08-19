SELECT DepartmentName
FROM Departments d
WHERE EXISTS
(
    SELECT 1
    FROM Employees e
    WHERE e.DepartmentID = d.DepartmentID
);
