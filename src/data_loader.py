# src/data_loader.py
import pandas as pd

def load_transactions(csv_path: str) -> pd.DataFrame:
    """
    Load transactions CSV, parse dates, fill missing categories.
    """
    df = pd.read_csv(csv_path, parse_dates=['date'])
    if 'category' not in df.columns:
        df['category'] = 'Uncategorized'
    else:
        df['category'] = df['category'].fillna('Uncategorized')
    return df

if __name__ == "__main__":
    df = load_transactions("data/sample_transactions.csv")
    print(df.head())
