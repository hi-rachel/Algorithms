select C.car_id,C.car_type,Round((daily_fee/100)*(100-discount_rate)*30) as Fee
from (select car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as H
group by H.Car_id
having Max(end_date)<'2022-11-01')as H join CAR_RENTAL_COMPANY_CAR as C
on H.car_id = C.car_id
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as P 
on P.car_type = C.car_type
where C.car_type in ("세단","SUV") and duration_type like "30일%"
and (daily_fee/100)*(100-discount_rate)*30 between 500000 and 2000000
order by Fee desc ,car_type