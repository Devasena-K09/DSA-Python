SELECT Name,
       Salary
FROM Employees
WHERE Salary =
(
    SELECT MAX(Salary)
    FROM Employees
    WHERE DepartmentID =
    (
        SELECT DepartmentID
        FROM Departments
        WHERE DepartmentName = 'IT'
    )
);
