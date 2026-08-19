SELECT EmployeeID,
       Name,
       Salary,
       RANK() OVER(
           ORDER BY Salary DESC
       ) AS RankNumber
FROM Employees;
