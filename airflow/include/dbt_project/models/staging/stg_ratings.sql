with src as (
    select
        rating,
        "userId",
        "movieId",
        "timestamp"
    from {{ source ('postgres', 'rawratings') }}
)
select * from src
