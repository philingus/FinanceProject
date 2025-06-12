# src/main.py
import argparse
from data_loader import load_transactions
from categorizer import apply_categorization
from analyzer import monthly_summary, overall_category_totals
from visualizer import plot_monthly_trends, plot_category_pie

def main():
    p = argparse.ArgumentParser()
    p.add_argument('-i','--input',  required=True, help="CSV of transactions")
    p.add_argument('-s','--savefig', help="Folder to save figures")
    args = p.parse_args()

    # 1. Load & preprocess
    df = load_transactions(args.input)

    # 2. Categorize
    df = apply_categorization(df)

    # 3. Analyze
    summary = monthly_summary(df)
    totals  = overall_category_totals(df)

    # 4. Plot or save
    if args.savefig:
        import os, matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        os.makedirs(args.savefig, exist_ok=True)

        # monthly trends
        plot_monthly_trends(summary)
        plt.savefig(f"{args.savefig}/monthly_trends.png")
        plt.clf()

        # category pie
        plot_category_pie(totals)
        plt.savefig(f"{args.savefig}/category_pie.png")
        plt.clf()

        print(f"Saved figures to folder: {args.savefig}")

    else:
        plot_monthly_trends(summary)
        plot_category_pie(totals)

if __name__=="__main__":
    main()
