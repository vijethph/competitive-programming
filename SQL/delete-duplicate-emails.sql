-- https://leetcode.com/problems/delete-duplicate-emails/

DELETE p1 from Person p1
inner join Person p2
where p1.id > p2.id and p1.email=p2.email;