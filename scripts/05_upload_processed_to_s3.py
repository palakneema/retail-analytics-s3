import boto3
import os

BUCKET_NAME = "retail-analytics-learning-bucket"
LOCAL_PROCESSED_PATH = "data/processed"
S3_PREFIX = "processed/"

s3 = boto3.client("s3")

def upload_folder(local_path, s3_prefix):
    for root, _, files in os.walk(local_path):
        for file in files:
            local_file = os.path.join(root, file)
            s3_key = os.path.join(
                s3_prefix,
                os.path.relpath(local_file, local_path)
            ).replace("\\", "/")

            s3.upload_file(local_file, BUCKET_NAME, s3_key)
            print(f"⬆ Uploaded: {s3_key}")

if __name__ == "__main__":
    upload_folder(LOCAL_PROCESSED_PATH, S3_PREFIX)
    print("✅ Processed data uploaded to S3")
