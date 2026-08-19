SELECT e1.Name,
       e1.Salary
FROM Employees e1
WHERE e1.Salary >
(
    SELECT AVG(e2.Salary)
    FROM Employees e2
    WHERE e1.DepartmentID = e2.DepartmentID
);
