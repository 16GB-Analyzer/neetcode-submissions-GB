-- Write your query below
Select employee_id,
CASE 
    WHEN employee_id%2!=0 and name not like 'M%' then salary 
    ELSE 0
    end as bonus
from employees
order by employee_id asc;



