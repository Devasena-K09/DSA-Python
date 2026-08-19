SELECT Name
FROM Employees
WHERE DepartmentID IN
(
    SELECT DepartmentID
    FROM Departments
    WHERE Location = 'Bangalore'
);
