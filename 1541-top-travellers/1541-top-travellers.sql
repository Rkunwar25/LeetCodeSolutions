# Write your MySQL query statement below
select u.name,IFNULL(SUM(r.distance), 0) as travelled_distance
from users u
left join rides r on u.id=r.user_id
group by user_id
order by travelled_distance desc,name asc