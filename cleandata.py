# ───────────────────────────────────────────────
# STANDARD SETUP (Formatting & Display)
# ───────────────────────────────────────────────
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

plt.rc("figure", figsize=(10, 6))
np.set_printoptions(precision=4)

pd.set_option("display.precision", 4)
pd.set_option("display.max_columns", 20)
pd.set_option("display.max_rows", 30)
pd.set_option("display.max_colwidth", 80)


def main():
    # ───────────────────────────────────────────────
    # Q1: Load dataset
    # ───────────────────────────────────────────────
    url = "https://raw.githubusercontent.com/adylw/Tests/refs/heads/main/test1Data2026.csv"

    try:
        df = pd.read_csv(url)
        print("Original Dataset:\n", df.head(), "\n")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return

    # ───────────────────────────────────────────────
    # Q2: Remove rows containing "skip me"
    # ───────────────────────────────────────────────
    try:
        mask = df.astype(str).apply(
            lambda row: row.str.contains("skip me", case=False).any(), axis=1
        )
        df = df[~mask].copy()
        print("After removing 'skip me' rows:\n", df.head(), "\n")
    except Exception as e:
        print(f"Error filtering rows: {e}")

    # ───────────────────────────────────────────────
    # Q3: Drop columns with all NA
    # ───────────────────────────────────────────────
    df.dropna(axis=1, how='all', inplace=True)

    # ───────────────────────────────────────────────
    # Q4: Remove rows with ≥ 4 NA values
    # ───────────────────────────────────────────────
    df = df[df.isna().sum(axis=1) < 4]

    # ───────────────────────────────────────────────
    # Q5: Fill NA in 'L' with median
    # ───────────────────────────────────────────────
    if 'L' in df.columns:
        df['L'] = df['L'].fillna(df['L'].median())

    # ───────────────────────────────────────────────
    # Q6: Drop duplicate rows
    # ───────────────────────────────────────────────
    df.drop_duplicates(inplace=True)

    # ───────────────────────────────────────────────
    # Q7: Replace stdDev ≤ 0 with NA
    # ───────────────────────────────────────────────
    if 'stdDev' in df.columns:
        df['stdDev'] = df['stdDev'].where(df['stdDev'] > 0, np.nan)

    # ───────────────────────────────────────────────
    # Q8: Backward fill stdDev
    # ───────────────────────────────────────────────
    if 'stdDev' in df.columns:
        df['stdDev'] = df['stdDev'].bfill()

    # ───────────────────────────────────────────────
    # Q9: Plot Month vs stdDev
    # ───────────────────────────────────────────────
    try:
        plt.plot(df['Month'], df['stdDev'], marker='o')
        plt.xlabel("Month")
        plt.ylabel("stdDev (kg)")
        plt.title("Month vs stdDev (kg)")
        plt.grid()

        plot_path = "test1.jpg"
        plt.savefig(plot_path)  # SAVE FIRST
        plt.show()

    except Exception as e:
        print(f"Plotting error: {e}")

    # ───────────────────────────────────────────────
    # Q10: Convert column names to UPPERCASE
    # ───────────────────────────────────────────────
    df.columns = [col.upper() for col in df.columns]

    # ───────────────────────────────────────────────
    # Q11: Sort by STDDEV descending
    # ───────────────────────────────────────────────
    if 'STDDEV' in df.columns:
        df.sort_values('STDDEV', ascending=False, inplace=True)

    # ───────────────────────────────────────────────
    # Q12: Print row with maximum L
    # ───────────────────────────────────────────────
    if 'L' in df.columns:
        max_row = df.loc[df['L'].idxmax()]
        print("Row with MAX L:\n", max_row, "\n")

    # ───────────────────────────────────────────────
    # Q13: Percent change of STDDEV
    # ───────────────────────────────────────────────
    if 'STDDEV' in df.columns:
        df['PCSTD'] = df['STDDEV'].pct_change() * 100

    # ───────────────────────────────────────────────
    # Q14: Save cleaned dataset
    # ───────────────────────────────────────────────
    csv_path = "test1.csv"
    df.to_csv(csv_path, index=False)

    # ───────────────────────────────────────────────
    # Final File Check
    # ───────────────────────────────────────────────
    print("File Check:\n")
    for file in [plot_path, csv_path]:
        if os.path.exists(file):
            print(f"{file} exists | size = {os.path.getsize(file)} bytes")
        else:
            print(f"{file} NOT found")


# Run program
if __name__ == "__main__":
    main()
