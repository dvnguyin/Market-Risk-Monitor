import os
from pathlib import Path
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

OUT_DIR = Path("data_processed")
OUT_DIR.mkdir(exist_ok=True)

SERIES = {
    "CPI": "CPIAUCSL",          # Inflation
    "UNRATE": "UNRATE",         # Unemployment
    "FEDFUNDS": "FEDFUNDS",     # Fed Funds Rate
    "DGS10": "DGS10",           # 10Y Treasury
    "SP500": "SP500",           # S&P 500
}

def fetch_series(series_id: str, api_key: str) -> pd.DataFrame:
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    data = r.json()["observations"]
    df = pd.DataFrame(data)[["date", "value"]]
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"])
    return df

def main():
    api_key = os.getenv("FRED_API_KEY")
    if not api_key:
        raise ValueError("Missing FRED_API_KEY in .env")

    frames = []
    for name, sid in SERIES.items():
        df = fetch_series(sid, api_key)
        df["series"] = name
        df["series_id"] = sid
        frames.append(df)

    out = pd.concat(frames, ignore_index=True)
    out_path = OUT_DIR / "fred_observations.csv"
    out.to_csv(out_path, index=False)
    print(f"✅ Saved {len(out)} rows to {out_path}")

if __name__ == "__main__":
    main()
