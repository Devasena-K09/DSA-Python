SELECT *
FROM
(
    SELECT Name,
           DepartmentID,
           Salary,
           DENSE_RANK() OVER(
               PARTITION BY DepartmentID
               ORDER BY Salary DESC
           ) AS SalaryRank
    FROM Employees
) RankedEmployees
WHERE SalaryRank <= 3;
