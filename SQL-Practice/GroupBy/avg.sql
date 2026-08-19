SELECT DepartmentID,
       AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY DepartmentID;
