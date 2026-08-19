SELECT EmployeeID,
       Name,
       Salary,
       SUM(Salary) OVER(
           ORDER BY EmployeeID
       ) AS RunningTotal
FROM Employees;
