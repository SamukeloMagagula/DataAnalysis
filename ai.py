import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ───────────────────────────────────────────────
# Q1–Q3: Read CSV and skip comment rows
# ───────────────────────────────────────────────
url = "https://raw.githubusercontent.com/adylw/Tutorials/refs/heads/main/wfa_girls_0-to-13-weeks_zscores.csv"

# Better way: read all lines and filter out comment-like rows
df = pd.read_csv(url, comment=None)  # comment=None keeps everything initially

# Remove rows that look like useless comments
mask_useless = df.astype(str).apply(
    lambda row: row.str.contains("useless", case=False).any(), axis=1
)
df = df[~mask_useless].copy()

# Also drop fully empty rows
df = df.dropna(how='all')

print("After cleaning comment rows & empty rows:")
print(df.head(10))
print("\nShape:", df.shape, "\n")

# Reset index after filtering
df.reset_index(drop=True, inplace=True)

# ───────────────────────────────────────────────
# Q4: Drop rows with more than 1 NA (i.e. keep rows with ≤1 NA)
# ───────────────────────────────────────────────
# thresh = minimum number of NON-NA values required
# so thresh = len(df.columns) - 1  →  allows max 1 NA
df.dropna(thresh=len(df.columns) - 1, inplace=True)

# ───────────────────────────────────────────────
# Q5: Drop columns that are entirely NA
# ───────────────────────────────────────────────
df.dropna(axis=1, how='all', inplace=True)

print("\nAfter dropping bad rows & empty columns:")
print(df.isna().sum())
print(df.head())

# ───────────────────────────────────────────────
# Q6: Fill NA in 'S' column with 0
# ───────────────────────────────────────────────
df['S'] = df['S'].fillna(0)

# ───────────────────────────────────────────────
# Q7: Drop duplicate rows
# ───────────────────────────────────────────────
df.drop_duplicates(inplace=True)

# ───────────────────────────────────────────────
# Q8: Replace SD0 values <= 0 with NaN
# ───────────────────────────────────────────────
df['SD0'] = df['SD0'].where(df['SD0'] > 0, np.nan)

# ───────────────────────────────────────────────
# Q9: Forward fill SD0
# ───────────────────────────────────────────────
df['SD0'] = df['SD0'].ffill()

# ───────────────────────────────────────────────
# Q10–Q11: Plot Week vs SD0
# ───────────────────────────────────────────────
plt.figure(figsize=(9, 5))
plt.plot(df['Week'], df['SD0'], marker='o', color='teal', linewidth=1.5)
plt.xlabel('Week')
plt.ylabel('SD0 (kg)')
plt.title('Weight-for-Age SD0 – Girls 0–13 weeks')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ───────────────────────────────────────────────
# Q12: Plot Week vs SD0, SD2, SD1neg (no 'Day' column exists)
# ───────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
for col, marker, color in zip(
    ['SD0', 'SD2', 'SD1neg'],
    ['o', 's', '^'],
    ['teal', 'coral', 'purple']
):
    ax.plot(df['Week'], df[col], marker=marker, label=col, color=color, linewidth=1.2)

ax.set_xlabel('Week')
ax.set_ylabel('Weight (kg)')
ax.set_title('Weight-for-Age SD curves – Girls 0–13 weeks')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ───────────────────────────────────────────────
# Q13: Save last plot
# ───────────────────────────────────────────────
plot_path = 'wfa_girls_sd_curves.png'
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {plot_path}\n")

# ───────────────────────────────────────────────
# Q14: Scale SD0 by 100 (→ grams?)
# ───────────────────────────────────────────────
df['SD0'] = df['SD0'] * 100

# ───────────────────────────────────────────────
# Q15: Column names to title case
# ───────────────────────────────────────────────
df.columns = [c.title() for c in df.columns]

# ───────────────────────────────────────────────
# Q16: Sort descending by Sd0 (note case!)
# ───────────────────────────────────────────────
df.sort_values('Sd0', ascending=False, inplace=True)

# ───────────────────────────────────────────────
# Q17: Min / closest-to-mean / max of S
# ───────────────────────────────────────────────
s = df['S']
mean_idx = (s - s.mean()).abs().idxmin()

print("Q17 – Statistics for column 'S':")
print(f"  min  = {s.min():.5f}  at index {s.idxmin()}")
print(f"  mean = {s.mean():.5f}  closest at index {mean_idx}")
print(f"  max  = {s.max():.5f}  at index {s.idxmax()}\n")

# ───────────────────────────────────────────────
# Q18: Percent change of Sd0
# ───────────────────────────────────────────────
df['Pcsdx'] = df['Sd0'].pct_change() * 100

# ───────────────────────────────────────────────
# Q19: Save cleaned data
# ───────────────────────────────────────────────
csv_path = 'wfa_girls_cleaned.csv'
df.to_csv(csv_path, index=False)
print(f"Cleaned data saved to: {csv_path}\n")

# ───────────────────────────────────────────────
# Q20: Check files
# ───────────────────────────────────────────────
for path in [plot_path, csv_path]:
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"{path:30} | exists = True | size = {size:,} bytes")
    else:
        print(f"{path:30} | exists = False")