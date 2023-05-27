-- https://leetcode.com/problems/customers-who-never-order/

select c1.name as 'Customers' from Customers c1
left join Orders c2 on c2.customerId = c1.id
where c2.customerId IS NULL;