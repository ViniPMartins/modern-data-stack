{{ config(
    schema='ouro',
    materialized='view'
) }}

with ouro as (
    SELECT * from {{ ref('prt_faturamento') }}
),
transform as (
    select 
        f.shipped_date as data_entrega,
        sum(f.quantity) as quantidade,
        sum(f.unit_price * f.quantity) as total_faturamento
    from ouro f
    group by f.shipped_date 
    order by f.shipped_date 
)
SELECT * from transform