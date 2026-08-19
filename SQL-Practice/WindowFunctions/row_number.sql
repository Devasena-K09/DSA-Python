SELECT EmployeeID,
       Name,
       Salary,
       ROW_NUMBER() OVER(
           ORDER BY Salary DESC
       ) AS RowNum
FROM Employees;
