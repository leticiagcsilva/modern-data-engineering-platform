"""Backward-compatible S3 loading wrapper."""

import pandas as pd

from src.load_to_s3 import upload_dataframe_to_s3


def upload_to_s3(df: pd.DataFrame, bucket_name: str, s3_path: str):
    """Preserve the original loading interface."""
    upload_dataframe_to_s3(dataset=df, bucket_name=bucket_name, object_key=s3_path)
