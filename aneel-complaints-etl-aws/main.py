from scripts.extract import extract_aneel_data
from scripts.transform import transform_data
from scripts.load import upload_to_s3

if __name__ == "__main__":
    raw_data = extract_aneel_data()
    processed_data = transform_data(raw_data)
    upload_to_s3(processed_data, bucket_name="aneel-etl-dados", s3_path="aneel/complaints/2025/complaints.csv")
