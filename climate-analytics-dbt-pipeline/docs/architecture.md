# Architecture Overview

## System Overview

This repository implements a lightweight analytics engineering pipeline for climate data. The design separates ingestion from transformation:

- Python is responsible for pulling raw historical observations from the Open-Meteo API and writing a reproducible CSV seed.
- dbt is responsible for data transformation, documentation, and model-level testing.
- DuckDB provides a fast local analytical engine for development and execution.

The result is a compact but production-oriented workflow that is easy to run locally and easy to extend.

## Data Source

The pipeline uses the Open-Meteo archive API as its upstream data source. The extraction script fetches daily observations for the capital cities of Brazil's Northeast region across a fixed historical window from 2020 through 2024.

Captured fields include:

- `date`
- `city`
- `state`
- `temperature_max`
- `temperature_min`
- `precipitation`

The API is only used during seed generation. Once the seed file exists, the project can be executed repeatedly without depending on a live upstream service.

## Modeling Layers

### Seed Layer

`seeds/daily_climate_northeast_capitals.csv` stores the extracted raw dataset in a reproducible format suitable for local development and versioned project structure.

### Staging Layer

`models/staging/stg_climate.sql` standardizes the seed data by:

- casting dates and numeric values
- normalizing city names
- preserving the original observation grain

This layer acts as the clean analytical foundation for downstream models.

### Mart Layer

`models/marts/core/mart_climate_summary.sql` aggregates the staged dataset into a yearly climate summary by city and state. It is designed as an analytics-ready output for reporting, exploration, or dashboard consumption.

## Transformation Flow

```text
Open-Meteo API
  -> scripts/generate_climate_seed.py
  -> seeds/daily_climate_northeast_capitals.csv
  -> dbt seed
  -> models/staging/stg_climate.sql
  -> models/marts/core/mart_climate_summary.sql
  -> analytics-ready yearly climate summary
```

## Output Datasets

### `stg_climate`

Observation-level standardized climate data with typed columns and normalized dimensions.

### `mart_climate_summary`

Yearly aggregated dataset with:

- city
- state
- year
- average max temperature
- average min temperature
- total precipitation

This output is suitable for exploratory analytics, operational reporting, or serving as an input to downstream semantic layers.

## Possible Production Extensions

- Add source freshness checks and stronger schema tests
- Introduce incremental materializations for longer date ranges
- Parameterize extraction windows and target regions
- Replace local execution with orchestrated scheduled runs
- Publish curated outputs to a cloud warehouse
- Feed mart outputs into dashboards, notebooks, or anomaly detection workflows
