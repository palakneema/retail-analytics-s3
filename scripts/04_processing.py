import pandas as pd
import os

RAW_PATH = "data/raw/SampleSuperstore.csv"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

def process_data():
    print("📊 Reading raw dataset...")
    df = pd.read_csv(RAW_PATH)

    # Clean column names
    df.columns = (
        df.columns
        .str.replace('\u00a0', ' ', regex=False)
        .str.strip()
    )

    print(" Columns available:")
    print(df.columns.tolist())

    # ---- KPI Summary ----
    kpi = {
        "total_sales": df["Sales"].sum(),
        "total_profit": df["Profit"].sum(),
        "total_quantity": df["Quantity"].sum()
    }

    pd.DataFrame([kpi]).to_csv(
        f"{PROCESSED_PATH}/kpi_summary.csv",
        index=False
    )

    # ---- Sales by Category ----
    df.groupby("Category")["Sales"].sum().reset_index().to_csv(
        f"{PROCESSED_PATH}/sales_by_category.csv",
        index=False
    )

    # ---- Profit by Category ----
    df.groupby("Category")["Profit"].sum().reset_index().to_csv(
        f"{PROCESSED_PATH}/profit_by_category.csv",
        index=False
    )

    # ---- Sales by Region ----
    df.groupby("Region")["Sales"].sum().reset_index().to_csv(
        f"{PROCESSED_PATH}/sales_by_region.csv",
        index=False
    )

    print("✅ Processing completed successfully!")

if __name__ == "__main__":
    process_data()
