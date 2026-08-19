SELECT EmployeeID,
       Name,
       Salary,
       LAG(Salary) OVER(
           ORDER BY Salary
       ) AS PreviousSalary,
       LEAD(Salary) OVER(
           ORDER BY Salary
       ) AS NextSalary
FROM Employees;
