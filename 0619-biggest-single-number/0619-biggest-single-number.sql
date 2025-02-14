/* Write your PL/SQL query statement below */
Select max(num) as num from(
select num from MyNumbers
group by num
having count(*)=1;
)