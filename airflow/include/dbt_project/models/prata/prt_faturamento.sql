with fat as (
    select
        ord.order_id,
        o.customer_id,
        c.company_name,
        o.order_date,
        o.shipped_date,
        o.ship_address,
        o.ship_city,
        o.ship_region,
        o.ship_country,
        o.ship_postal_code,
        ord.product_id,
        p.product_name,
        ord.unit_price,
        ord.quantity,
        ord.discount
    from {{ source ('postgres', 'order_details' )}} ord, 
        {{ source ('postgres', 'products')}} p, 
        {{ source ('postgres', 'orders')}} o, 
        {{ source ('postgres', 'customers') }} c 
    where ord.product_id = p.product_id
    and ord.order_id = o.order_id 
    and c.customer_id = o.customer_id 
)
select * from fat