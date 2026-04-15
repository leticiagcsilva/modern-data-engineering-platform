# ANEEL Complaints ETL Pipeline (AWS)

This project implements a cloud-based ETL pipeline that ingests public complaint data from ANEEL, applies data transformation and standardization, and stores the processed dataset in AWS S3.

## Overview

`aneel-complaints-etl-aws` is a compact, production-oriented ETL subproject designed to demonstrate a realistic external-data ingestion flow. It extracts complaint records from ANEEL's public CKAN API, standardizes the dataset with Pandas, and uploads the processed output to Amazon S3.

The project keeps the implementation intentionally lightweight while still reflecting core data engineering concerns: modular pipeline design, reproducible local execution, cloud storage integration, and clear operational documentation.

## Data Source

The upstream source is ANEEL's open data portal, accessed through a CKAN datastore API endpoint. The current pipeline retrieves public complaint records from a defined resource and converts the response into a tabular dataset for downstream processing.

## Architecture

```text
ANEEL CKAN API
  -> ingestion
  -> transformation
  -> processed dataset
  -> AWS S3
```

### Repository Structure

```text
aneel-complaints-etl-aws/
├── docs/
│   └── architecture.md
├── scripts/
│   ├── extract.py
│   ├── load.py
│   └── transform.py
├── src/
│   ├── ingestion.py
│   ├── load_to_s3.py
│   ├── pipeline.py
│   └── transformation.py
├── .gitignore
├── main.py
├── pyproject.toml
├── README.md
└── taskipy.toml
```

## Pipeline Steps

### 1. Ingestion

`src/ingestion.py` requests complaint data from the ANEEL CKAN API and materializes the JSON payload as a Pandas DataFrame.

### 2. Transformation

`src/transformation.py` normalizes column names, removes records missing key fields, and standardizes the complaint reference date.

### 3. Load

`src/load_to_s3.py` converts the processed dataset to CSV and uploads it to a target S3 bucket and object key.

### 4. Orchestration

`src/pipeline.py` coordinates the end-to-end flow and supports environment-based configuration for the S3 destination.

## Tech Stack

- `Python`
- `Requests`
- `Pandas`
- `Boto3`
- `Poetry`
- `Taskipy`
- `AWS S3`

## How to Run

### 1. Install dependencies

```bash
poetry install
```

### 2. Configure AWS credentials

The pipeline uses your local AWS credentials. You can configure them with:

```bash
aws configure
```

Or use environment variables and an existing AWS profile if you already have local cloud access configured.

### 3. Configure the S3 destination

Optional environment variables:

```bash
export AWS_S3_BUCKET="your-target-bucket"
export AWS_S3_OBJECT_KEY="aneel/complaints/2025/complaints.csv"
```

If these are not provided, the pipeline uses the defaults defined in `src/pipeline.py`.

### 4. Run the ETL

```bash
poetry run task run
```

This executes:

- API extraction from ANEEL
- in-memory transformation
- CSV upload to S3

### 5. Output location

By default, the processed dataset is uploaded to:

- bucket: `aneel-etl-dados`
- object key: `aneel/complaints/2025/complaints.csv`

## Engineering Practices

- Clear separation between ingestion, transformation, load, and orchestration concerns
- Local reproducibility through Poetry-managed dependencies
- Cloud-native storage handoff using S3
- Backward-compatible wrappers preserved in `scripts/`
- Small, maintainable codebase with straightforward extension points

## Potential Improvements

- Partition S3 outputs by ingestion date or complaint reference period
- Add schema validation before loading
- Introduce structured logging and execution monitoring
- Support incremental ingestion and pagination across larger API result sets
- Add orchestration with Airflow, Dagster, or AWS Step Functions
- Publish curated outputs to Athena, Glue, or Redshift

## Why This Project Matters

This project demonstrates a realistic ETL pattern that appears frequently in production data platforms: extracting public operational data from an external API, standardizing it into a clean dataset, and landing the result in cloud object storage for downstream analytics or reporting.

## Additional Documentation

- Architecture details: [docs/architecture.md](/Users/leticiagomesdacostaesilva/Documents/1-Professional/Github/REFACTORING/modern-data-engineering-platform/aneel-complaints-etl-aws/docs/architecture.md)
