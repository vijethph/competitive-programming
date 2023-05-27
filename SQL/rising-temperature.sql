-- https://leetcode.com/problems/rising-temperature/

select c1.id
from Weather c1 cross join Weather c2
where datediff(c1.recordDate, c2.recordDate) = 1 and  c1.temperature > c2.temperature;