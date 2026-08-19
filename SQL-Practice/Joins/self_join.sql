SELECT E1.Name AS Employee,
       E2.Name AS Manager
FROM Employees E1
LEFT JOIN Employees E2
ON E1.ManagerID = E2.EmployeeID;
