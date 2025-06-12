# src/visualizer.py
import matplotlib.pyplot as plt

def plot_monthly_trends(df_summary):
    pivot = df_summary.pivot(index='month',
                             columns='predicted_category',
                             values='amount').fillna(0)
    pivot.plot(kind='line', figsize=(10,6))
    plt.title("Monthly Spending by Category")
    plt.xlabel("Month")
    plt.ylabel("Amount ($)")
    plt.tight_layout()
    plt.show()

def plot_category_pie(series_totals):
    series_totals.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
    plt.ylabel('')
    plt.title("Overall Category Breakdown")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    from data_loader import load_transactions
    from categorizer import apply_categorization
    from analyzer import monthly_summary, overall_category_totals

    df = load_transactions("data/sample_transactions.csv")
    df = apply_categorization(df)
    summary = monthly_summary(df)
    totals  = overall_category_totals(df)
    plot_monthly_trends(summary)
    plot_category_pie(totals)
