with src as (
    select * from {{ source ('postgres', 'rawmovies') }}
)
select * from src
