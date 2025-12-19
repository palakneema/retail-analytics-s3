import os
import boto3

# -------- CONFIG --------
BUCKET_NAME = "retail-analytics-learning-bucket"
LOCAL_REPORTS_PATH = "reports"
S3_REPORTS_PREFIX = "reports/"

s3 = boto3.client("s3")

def upload_reports_to_s3():
    print("☁️ Uploading reports to S3...")

    for file_name in os.listdir(LOCAL_REPORTS_PATH):
        local_file_path = os.path.join(LOCAL_REPORTS_PATH, file_name)
        s3_key = S3_REPORTS_PREFIX + file_name

        s3.upload_file(local_file_path, BUCKET_NAME, s3_key)
        print(f"✅ Uploaded: {s3_key}")

    print("🎉 All reports uploaded successfully.")

if __name__ == "__main__":
    upload_reports_to_s3()
