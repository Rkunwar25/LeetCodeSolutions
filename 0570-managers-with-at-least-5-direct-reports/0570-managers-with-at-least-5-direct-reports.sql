-- # Write your MySQL query statement below
-- select name
-- from employee
-- where count(managerId)>=all(select count(managerId)
-- from employee
-- group by managerId);
SELECT e1.name
FROM Employee e1
JOIN Employee e2
ON e1.id = e2.managerId
GROUP BY e1.id, e1.name
HAVING COUNT(e2.id) >= 5;
