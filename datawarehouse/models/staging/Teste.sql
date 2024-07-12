with source_movies AS (
    SELECT 
        title,
        genres,
        "movieId"
    FROM {{ source ('postgres', 'mv_movies') }}
),
ratings as (
    select
        a."movieId",
        a.title,
        a.genres
    from source_movies a
)
select * from ratings