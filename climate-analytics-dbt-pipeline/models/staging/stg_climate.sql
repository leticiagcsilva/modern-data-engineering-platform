with raw as (
    select
        cast(date as date) as observation_date,
        lower(city) as city,
        state,
        cast(temperature_max as float) as temperature_max,
        cast(temperature_min as float) as temperature_min,
        cast(precipitation as float) as precipitation
    from {{ ref('daily_climate_northeast_capitals') }}
)

select *
from raw
