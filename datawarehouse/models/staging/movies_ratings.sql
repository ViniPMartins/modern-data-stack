with source_movies AS (
    SELECT 
        title,
        genres,
        "movieId"
    FROM {{ source ('postgres', 'mv_movies') }}
),
source_ratings AS (
    SELECT * FROM {{ source ('postgres', 'rt_ratings') }}
),
ratings as (
    select
        a."movieId",
        a.title,
        a.genres,
        b.rating,
        b.timestamp
    from
        source_movies a, source_ratings b
    where
        a."movieId" = b."movieId"
)
select * from ratings