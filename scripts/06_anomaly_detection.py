import pandas as pd
import os
from scipy import stats

RAW_PATH = "data/raw/SampleSuperstore.csv"
ANOMALY_PATH = "data/processed/anomalies"

os.makedirs(ANOMALY_PATH, exist_ok=True)

def detect_anomalies():
    print("🚨 Detecting anomalies...")

    df = pd.read_csv(RAW_PATH)
    df.columns = df.columns.str.strip()

    # Z-score on Sales
    df["z_score"] = stats.zscore(df["Sales"])
    anomalies = df[df["z_score"].abs() > 3]

    anomalies.to_csv(
        f"{ANOMALY_PATH}/sales_anomalies.csv",
        index=False
    )

    print("✅ Anomaly detection completed!")

if __name__ == "__main__":
    detect_anomalies()
