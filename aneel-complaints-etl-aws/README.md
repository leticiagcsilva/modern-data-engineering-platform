# ETL of ANEEL Complaint Data to AWS

This subproject is part of the `Cloud_Data_Engineer` repository.

It demonstrates a simple yet powerful cloud data engineering pipeline using public complaint data from ANEEL (the Brazilian Electricity Regulatory Agency).

## What It Does

- **Extract**: Pulls public complaint data via the ANEEL CKAN API
- **Transform**: Cleans and standardizes the dataset using Pandas
- **Load**: Uploads the final CSV to an AWS S3 bucket

## Technologies Used

- Python
- Pandas
- Boto3 (AWS SDK for Python)
- Poetry
- Taskipy

## How to Run

```bash
# Install dependencies
poetry install

# Configure AWS credentials
aws configure

# Run ETL
poetry run task run

# Deploy to GitHub
poetry run task deploy
```

This project highlights real-world data engineering capabilities and cloud deployment practices.
