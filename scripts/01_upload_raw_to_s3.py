import os
import boto3

# ======================
# CONFIGURATION
# ======================
BUCKET_NAME = "retail-analytics-learning-bucket"
LOCAL_RAW_PATH = "data/raw"
S3_RAW_PREFIX = "raw"

# Create S3 client
s3 = boto3.client("s3")

def upload_raw_files():
    files = os.listdir(LOCAL_RAW_PATH)

    if not files:
        print("❌ No files found in data/raw")
        return

    for file in files:
        local_file_path = os.path.join(LOCAL_RAW_PATH, file)
        s3_key = f"{S3_RAW_PREFIX}/{file}"

        print(f"Uploading {file} to s3://{BUCKET_NAME}/{s3_key}")
        s3.upload_file(local_file_path, BUCKET_NAME, s3_key)

    print("✅ RAW data upload completed successfully")

if __name__ == "__main__":
    upload_raw_files()
