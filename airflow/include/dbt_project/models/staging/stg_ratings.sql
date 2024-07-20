with src as (
    select * from {{ source ('postgres', 'rawratings') }}
)
select * from src
