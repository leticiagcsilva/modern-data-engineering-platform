with base as (
    select
        city,
        state,
        extract(year from observation_date) as year,
        avg(temperature_max) as avg_temperature_max,
        avg(temperature_min) as avg_temperature_min,
        sum(precipitation) as total_precipitation
    from {{ ref('stg_climate') }}
    group by city, state, year
)

select *
from base
order by city, year
