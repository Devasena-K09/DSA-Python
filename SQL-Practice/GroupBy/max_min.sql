SELECT DepartmentID,
       MAX(Salary) AS HighestSalary,
       MIN(Salary) AS LowestSalary
FROM Employees
GROUP BY DepartmentID;
