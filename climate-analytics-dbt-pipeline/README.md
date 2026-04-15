# Climate Analytics dbt Pipeline

This project implements an end-to-end analytics engineering pipeline using dbt and DuckDB, transforming raw climate data into analytics-ready datasets through layered data modeling.

## Overview

`climate-analytics-dbt-pipeline` reframes a small educational dbt project as a production-oriented analytics engineering portfolio piece. The pipeline ingests historical climate observations from the Open-Meteo API, stores a reproducible local seed, standardizes the dataset in a staging layer, and publishes a business-friendly mart for downstream analytics.

The goal is not to simulate a full platform with unnecessary complexity. Instead, the project demonstrates how analytics engineers structure transformations, document semantic meaning, and create reusable analytical datasets with lightweight tooling.

## Data Context

The source data covers daily climate observations for the nine capital cities of Brazil's Northeast region between 2020-01-01 and 2024-12-31. Each record includes:

- observation date
- city and state
- maximum temperature
- minimum temperature
- daily precipitation

The Open-Meteo archive API is used only during seed generation. After the CSV seed is generated, the transformation flow is fully reproducible locally with dbt and DuckDB.

## Architecture

```text
Open-Meteo API
  -> seed generation
  -> dbt seed
  -> staging model
  -> mart model
  -> analytics-ready dataset
```

### Repository Structure

```text
climate-analytics-dbt-pipeline/
├── docs/
│   └── architecture.md
├── models/
│   ├── marts/
│   │   └── core/
│   │       └── mart_climate_summary.sql
│   ├── staging/
│   │   └── stg_climate.sql
│   └── schema.yml
├── scripts/
│   └── generate_climate_seed.py
├── seeds/
│   └── daily_climate_northeast_capitals.csv
├── .gitignore
├── dbt_project.yml
├── generate_open_meteo_seed.py
├── pyproject.toml
└── README.md
```

## Data Modeling Approach

The project follows a simple layered modeling pattern aligned with analytics engineering best practices:

- `seeds/`: reproducible raw input stored as CSV for local development
- `staging/`: type casting, normalization, and light cleanup
- `marts/core/`: analytics-oriented aggregations designed for consumption

### Models

- `stg_climate`
  Standardizes the seed into typed climate observations with normalized city names and numeric measures.

- `mart_climate_summary`
  Produces yearly climate summaries by city and state, including average temperatures and total precipitation.

This separation keeps ingestion concerns outside dbt while preserving a clean transformation boundary inside the project.

## Tech Stack

- `dbt-duckdb` for SQL-based transformations
- `DuckDB` as the local analytical engine
- `Python` for seed generation
- `Pandas` for shaping API responses into tabular data
- `Requests` for API access
- `Poetry` and `Taskipy` for dependency and command management

## How to Run

### 1. Install dependencies

```bash
poetry install
```

### 2. Configure dbt profile

Create or update `~/.dbt/profiles.yml` with a DuckDB profile named `climate_analytics_dbt_pipeline`.

Example:

```yaml
climate_analytics_dbt_pipeline:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: climate_analytics.duckdb
      threads: 4
```

### 3. Generate the local seed

```bash
poetry run python scripts/generate_climate_seed.py
```

Compatibility wrapper:

```bash
poetry run python generate_open_meteo_seed.py
```

### 4. Load the seed into DuckDB

```bash
poetry run task dbt_seed
```

### 5. Run the transformation models

```bash
poetry run task dbt_run
```

### 6. Generate dbt documentation

```bash
poetry run task dbt_docs_generate
poetry run task dbt_docs_serve
```

### 7. Run data quality tests

```bash
poetry run task dbt_test
```

### 8. Run the end-to-end pipeline

```bash
poetry run task dbt_all
```

## Engineering Practices

- Reproducible local development via `DuckDB`, `dbt seed`, and committed configuration
- Clear separation between ingestion logic and transformation logic
- Layered modeling with a distinct staging and mart boundary
- Schema-level documentation and lightweight tests in `models/schema.yml`
- Executable validation through `dbt test`
- Domain-oriented naming that makes analytical intent explicit

## Industrial / Analytics Relevance

This project mirrors a common analytics engineering pattern used in production:

- ingest external operational data
- convert it into a stable raw input artifact
- standardize the structure in staging
- publish curated business-facing datasets for analysis and reporting

The same approach can be extended to energy analytics, environmental monitoring, public-sector reporting, or downstream BI use cases.

## Future Improvements

- Add incremental models for larger climate history windows
- Expand data quality checks for nulls, duplicates, and accepted ranges
- Introduce orchestration with Airflow, Dagster, or GitHub Actions
- Swap DuckDB for a warehouse target such as BigQuery, Snowflake, or Redshift
- Expose the mart to dashboards or notebook-based analytics
- Add anomaly detection for precipitation and temperature shifts

## Why This Project Matters

Analytics engineering projects are strongest when they show more than SQL syntax. This repository demonstrates how to organize transformation assets, model data in layers, preserve reproducibility, and communicate engineering decisions in a way that feels closer to real production work than coursework.

## Additional Documentation

- Architecture details: [docs/architecture.md](/Users/leticiagomesdacostaesilva/Documents/1-Professional/Github/REFACTORING/modern-data-engineering-platform/climate-analytics-dbt-pipeline/docs/architecture.md)
