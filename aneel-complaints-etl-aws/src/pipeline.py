"""Pipeline orchestration for the ANEEL complaints ETL workflow."""

import os

from src.ingestion import fetch_aneel_complaints
from src.load_to_s3 import upload_dataframe_to_s3
from src.transformation import transform_aneel_complaints


DEFAULT_BUCKET_NAME = "aneel-etl-dados"
DEFAULT_OBJECT_KEY = "aneel/complaints/2025/complaints.csv"


def run_pipeline(bucket_name: str | None = None, object_key: str | None = None) -> None:
    """Execute the ETL flow from API extraction to S3 upload."""
    target_bucket = bucket_name or os.getenv("AWS_S3_BUCKET", DEFAULT_BUCKET_NAME)
    target_key = object_key or os.getenv("AWS_S3_OBJECT_KEY", DEFAULT_OBJECT_KEY)

    raw_complaints_df = fetch_aneel_complaints()
    transformed_complaints_df = transform_aneel_complaints(raw_complaints_df)
    upload_dataframe_to_s3(
        dataset=transformed_complaints_df,
        bucket_name=target_bucket,
        object_key=target_key,
    )
