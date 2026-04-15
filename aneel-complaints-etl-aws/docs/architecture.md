# Architecture Overview

## System Overview

This subproject implements a lightweight ETL pipeline that retrieves public complaint data from ANEEL's CKAN API, applies basic transformation and standardization, and stores the processed dataset in Amazon S3.

The design intentionally keeps the workflow simple:

- API ingestion is isolated from transformation logic
- transformation is handled in-memory with Pandas
- cloud storage is handled through a dedicated S3 loading step
- the pipeline can be executed locally with standard AWS credentials

## Data Source Description

The upstream source is the ANEEL open data portal, exposed through a CKAN datastore API endpoint. The pipeline retrieves complaint records from a public resource and converts the API payload into a tabular dataset for downstream processing.

Core source characteristics:

- public HTTP API
- JSON response format
- tabular complaint records
- suitable for batch-style extraction

## ETL Flow

```text
ANEEL CKAN API
  -> ingestion
  -> transformation
  -> processed dataset
  -> AWS S3
```

### Ingestion

`src/ingestion.py` requests complaint records from the public ANEEL API and converts the result into a Pandas DataFrame.

### Transformation

`src/transformation.py` standardizes column names, removes rows missing key fields, and converts the reference date to a datetime type.

### Load

`src/load_to_s3.py` serializes the transformed dataset as CSV and uploads it to a configured S3 object path.

### Orchestration

`src/pipeline.py` coordinates the end-to-end execution flow and supports configuration through environment variables for the target S3 location.

## Storage Flow

The pipeline currently writes a single CSV object to S3. This keeps the project easy to run locally while still demonstrating cloud storage integration and a realistic output handoff pattern.

Default target:

- bucket: `aneel-etl-dados`
- object key: `aneel/complaints/2025/complaints.csv`

## Possible Production Extensions

- partition the S3 output by ingestion date or reference period
- add structured logging and execution metrics
- validate schema and required fields before upload
- implement incremental extraction beyond the fixed batch limit
- orchestrate scheduled runs with Airflow, Dagster, or AWS-native tooling
- expose the curated dataset to Athena, Glue, or Redshift
