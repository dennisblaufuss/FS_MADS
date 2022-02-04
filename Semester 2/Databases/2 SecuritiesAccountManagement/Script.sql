use securitiesaccountmanagement
go

-- 1
select *
from securitiesaccountmanagement.`security`


-- 2
select * 
from securitiesaccountmanagement.`security`
where Security_id < 700000


-- 3
select * 
from securitiesaccountmanagement.`security`
where Security_id > 600000 and Security_id < 700000


-- 4
select Customer_id, Name
from securitiesaccountmanagement.customer
order by Name


-- 5
select *
from securitiesaccountmanagement.account
where Customer_id = (select Customer_id from securitiesaccountmanagement.customer where Name like 'M%ller, Erich')


-- 6
select *
from securitiesaccountmanagement.account acc
left join securitiesaccountmanagement.item it
on acc.Account_id = it.Account_id


-- 7
select *
from securitiesaccountmanagement.account acc
left join securitiesaccountmanagement.item it
on acc.Account_id = it.Account_id
left join securitiesaccountmanagement.`security` sec
on acc.Account_id = sec.Account_id


-- 8



-- 9



-- 10



-- 11
