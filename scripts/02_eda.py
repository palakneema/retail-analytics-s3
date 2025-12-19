import os
import pandas as pd
from ydata_profiling import ProfileReport

# ======================
# PATH CONFIG
# ======================
INPUT_FILE = "data/raw/SampleSuperstore.csv"
OUTPUT_DIR = "reports"
OUTPUT_FILE = "superstore_eda_report.html"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_eda():
    print("📊 Reading dataset...")
    df = pd.read_csv(INPUT_FILE)

    print("📈 Generating EDA report...")
    profile = ProfileReport(
        df,
        title="Superstore EDA Report",
        explorative=True
    )

    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    profile.to_file(output_path)

    print(f"✅ EDA report generated at: {output_path}")

if __name__ == "__main__":
    generate_eda()
