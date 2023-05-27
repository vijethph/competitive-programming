-- https://leetcode.com/problems/combine-two-tables/

select c1.firstName, c1.lastName, c2.city, c2.state
from Person c1 left join Address c2 on c1.personId = c2.personId;