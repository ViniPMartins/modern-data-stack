with src as (
    select
        title,
        genres,
        "movieId"
    from {{ source ('postgres', 'rawmovies') }}
)
select * from src
