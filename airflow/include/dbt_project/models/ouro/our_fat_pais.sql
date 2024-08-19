with prata as (
    SELECT * from {{ ref ('prt_faturamento') }}
),
transform as (
    select 
        f.ship_country as pais_entrega,
        sum(f.quantity) as quantidade,
        sum(f.unit_price * f.quantity) as total_faturamento
    from prata f
    group by f.ship_country 
    order by total_faturamento DESC
)
SELECT * from transform
