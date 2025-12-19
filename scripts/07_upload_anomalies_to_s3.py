import boto3
import os

BUCKET_NAME = "retail-analytics-learning-bucket"
LOCAL_ANOMALY_PATH = "data/processed/anomalies"
S3_PREFIX = "processed/anomalies"

s3 = boto3.client("s3")

def upload_anomalies():
    for file in os.listdir(LOCAL_ANOMALY_PATH):
        local_file = os.path.join(LOCAL_ANOMALY_PATH, file)
        s3_key = f"{S3_PREFIX}/{file}"
        s3.upload_file(local_file, BUCKET_NAME, s3_key)
        print(f"⬆ Uploaded: {s3_key}")

if __name__ == "__main__":
    upload_anomalies()
    print("✅ Anomalies uploaded to S3")
