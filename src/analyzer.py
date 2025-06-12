# src/analyzer.py
import pandas as pd

def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    df['month'] = df['date'].dt.to_period('M')
    return (
        df.groupby(['month','predicted_category'])['amount']
          .sum()
          .reset_index()
          .sort_values(['month','amount'], ascending=[True,False])
    )

def overall_category_totals(df: pd.DataFrame) -> pd.Series:
    return df.groupby('predicted_category')['amount']\
             .sum()\
             .sort_values(ascending=False)

def top_n_categories(df: pd.DataFrame, n:int=5) -> pd.Series:
    return overall_category_totals(df).head(n)

if __name__ == "__main__":
    from data_loader import load_transactions
    from categorizer import apply_categorization
    df = load_transactions("data/sample_transactions.csv")
    df = apply_categorization(df)
    print(monthly_summary(df).head())
    print("\nTop 5:", top_n_categories(df))
