SELECT EmployeeID,
       Name,
       Salary,
       DENSE_RANK() OVER(
           ORDER BY Salary DESC
       ) AS DenseRank
FROM Employees;
