SELECT Salary
FROM
(
    SELECT Salary,
           DENSE_RANK() OVER(
               ORDER BY Salary DESC
           ) AS SalaryRank
    FROM Employees
) RankedSalaries
WHERE SalaryRank = 3;
