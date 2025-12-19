import json
from datetime import datetime
import boto3

BUCKET_NAME = "retail-analytics-learning-bucket"
METADATA_KEY = "metadata/pipeline_run.json"

s3 = boto3.client("s3")

def write_metadata():
    metadata = {
        "pipeline_name": "retail-analytics-learning",
        "run_time": datetime.utcnow().isoformat(),
        "status": "SUCCESS",
        "outputs": [
            "raw/",
            "processed/",
            "processed/anomalies/",
            "reports/"
        ]
    }

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=METADATA_KEY,
        Body=json.dumps(metadata, indent=4)
    )

    print("📝 Metadata written to S3")

if __name__ == "__main__":
    write_metadata()
