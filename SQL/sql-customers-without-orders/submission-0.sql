-- Write your query below
Select customers.name from customers
where id NOT in (
    Select customer_id from orders);


