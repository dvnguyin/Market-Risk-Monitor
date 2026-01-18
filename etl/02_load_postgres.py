import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

CSV_PATH = "data_processed/fred_observations.csv"

def main():
    engine = create_engine(os.getenv("DATABASE_URL"))

    df = pd.read_csv(CSV_PATH, parse_dates=["date"])

    df.to_sql(
        "fred_observations",
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✅ Loaded {len(df)} rows into fred_observations")

if __name__ == "__main__":
    main()
