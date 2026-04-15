import boto3
import pandas as pd
from io import StringIO

def upload_to_s3(df: pd.DataFrame, bucket_name: str, s3_path: str):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket_name, Key=s3_path, Body=csv_buffer.getvalue())
