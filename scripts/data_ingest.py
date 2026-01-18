# Convert CSV to Parquet for faster I/O.

import os
import pandas as pd

def load_raw(path: str) -> pd.DataFrame:
    """
    Load the raw CSV Superstore dataset and return as DataFrame.
    Handles Windows-encoded CSVs.
    """
    try:
        df = pd.read_csv(path, low_memory=False, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(path, low_memory=False, encoding="latin1")
    return df


if __name__ == '__main__':
    infile = r"D:\Data analysis BI\Project\Superstore_analysis\data\raw\Sample - Superstore.csv"
    outfile = r"D:\Data analysis BI\Project\Superstore_analysis\data\raw\superstore.parquet"

    df = load_raw(infile)

    os.makedirs(os.path.dirname(outfile), exist_ok=True)

    df.to_parquet(outfile)
    print(f"Saved ingested data to {outfile}")
