with prata as (
    SELECT * from {{ ref ('prt_faturamento') }}
),
transform as (
    select 
        f.customer_id as cliente_id,
        f.company_name as cliente_nome,
        sum(f.quantity) as quantidade,
        sum(f.unit_price * f.quantity) as total_faturamento
    from prata f
    group by f.customer_id, f.company_name
    order by total_faturamento DESC
)
SELECT * from transform
