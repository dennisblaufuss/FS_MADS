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


-- 7 ERRROR in join
select *
from securitiesaccountmanagement.account acc
left join securitiesaccountmanagement.item it
on acc.Account_id = it.Account_id
left join securitiesaccountmanagement.`security` sec
on acc.Account_id = sec.Account_id


-- 8
select *
from securitiesaccountmanagement.`security` sec
left join securitiesaccountmanagement.item it
on sec.Security_id = it.Security_id
where sec.Price < it.Purchase_price 


-- 9



-- 10



-- 11



-- 12



-- 13



-- 14



-- 15



-- 16



-- 17



-- 18



-- 19
insert into securitiesaccountmanagement.customer
values(5, 'Blaufuss, Dennis', 'Walter-Hesselbach-Straße 54, 60389 Frankfurt')


-- 20
update securitiesaccountmanagement.account
set Customer_id = 5
where Account_id = 3


-- 21
delete from securitiesaccountmanagement.`security`
where Name = 'VEBA'

