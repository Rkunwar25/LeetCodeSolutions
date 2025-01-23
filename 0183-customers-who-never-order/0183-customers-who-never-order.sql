# Write your MySQL query statement below
select name as 'Customers'
from customers c
where id not in
(
    select customerid
    from orders
)