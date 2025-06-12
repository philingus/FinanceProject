# src/categorizer.py
from typing import Dict, List
import pandas as pd

KEYWORD_MAP: Dict[str, List[str]] = {
    'Groceries': ['walmart','whole foods','kroger'],
    'Dining':   ['restaurant','starbucks','burger'],
    'Travel':   ['uber','lyft','airbnb','delta'],
    'Utilities':['electric','water','gas','internet','verizon'],
}

def categorize_description(desc: str) -> str:
    text = desc.lower()
    for cat, keywords in KEYWORD_MAP.items():
        if any(kw in text for kw in keywords):
            return cat
    return 'Other'

def apply_categorization(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['predicted_category'] = df['description'].apply(categorize_description)
    return df

if __name__ == "__main__":
    from data_loader import load_transactions
    df = load_transactions("data/sample_transactions.csv")
    print(apply_categorization(df).head())
