with prata as (
    SELECT * from {{ ref ('prt_faturamento') }}
),
transform as (
    select 
        f.product_id as produto_id,
        f.product_name as produto_nome,
        sum(f.quantity) as quantidade,
        sum(f.unit_price * f.quantity) as total_faturamento
    from prata f
    group by f.product_id, f.product_name
    order by total_faturamento DESC
)
SELECT * from transform
