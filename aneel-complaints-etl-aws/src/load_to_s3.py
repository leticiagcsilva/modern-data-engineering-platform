"""AWS S3 loading utilities for the ANEEL complaints ETL pipeline."""

from io import StringIO

import boto3
import pandas as pd


def upload_dataframe_to_s3(
    dataset: pd.DataFrame, bucket_name: str, object_key: str
) -> None:
    """Serialize a DataFrame to CSV and upload it to Amazon S3."""
    csv_buffer = StringIO()
    dataset.to_csv(csv_buffer, index=False)

    s3_client = boto3.client("s3")
    s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=csv_buffer.getvalue())
