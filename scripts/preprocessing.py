# scripts/preprocess_large.py
import os
import pandas as pd
import pyarrow.parquet as pq

def preprocess_chunk(df_chunk: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess a chunk of airline delay data:
    - Remove canceled and diverted flights
    - Drop rows with missing DEPARTURE_DELAY or ARRIVAL_DELAY
    - Fill other numeric NaNs with 0
    - Convert categorical columns to string
    - Downcast numeric columns to reduce memory
    """
    # Filter flights and make a copy to avoid warnings
    df_chunk = df_chunk[(df_chunk['CANCELLED'] == 0) & (df_chunk['DIVERTED'] == 0)].copy()

    # Drop rows with missing delays
    df_chunk.dropna(subset=['DEPARTURE_DELAY', 'ARRIVAL_DELAY'], inplace=True)

    # Fill numeric NaNs
    numeric_cols = df_chunk.select_dtypes(include='number').columns
    df_chunk[numeric_cols] = df_chunk[numeric_cols].fillna(0)

    # Convert categorical columns to string
    cat_cols = ['AIRLINE', 'TAIL_NUMBER', 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT']
    for c in cat_cols:
        if c in df_chunk.columns:
            df_chunk[c] = df_chunk[c].astype(str)

    # Downcast numeric columns safely
    for col in numeric_cols:
        df_chunk[col] = pd.to_numeric(df_chunk[col], downcast='float')

    return df_chunk

if __name__ == '__main__':
    infile = r"D:\Data analysis BI\Project\airline-delay-analysis\data\raw\airlines_data.parquet"
    outfile = r"D:\Data analysis BI\Project\airline-delay-analysis\data\processed\airlines_data_preproc.parquet"

    print("Reading parquet file in chunks...")
    pq_file = pq.ParquetFile(infile)
    dfs = []

    for i in range(pq_file.num_row_groups):
        print(f"Processing row group {i+1}/{pq_file.num_row_groups}...")
        table = pq_file.read_row_group(i)
        df_chunk = table.to_pandas()
        df_clean_chunk = preprocess_chunk(df_chunk)
        dfs.append(df_clean_chunk)

    print("Concatenating all chunks...")
    df_clean = pd.concat(dfs, ignore_index=True)

    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    df_clean.to_parquet(outfile, index=False)
    print(f"Saved preprocessed data to {outfile}")
