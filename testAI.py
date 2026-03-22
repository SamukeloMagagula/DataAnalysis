import pandas as pd, numpy as np, matplotlib.pyplot as plt, requests, os

URL = "https://raw.githubusercontent.com/adylw/Tutorials/refs/heads/main/wfa_girls_0-to-13-weeks_zscores.csv"

# Q1 – Read CSV from URL
df = pd.read_csv(URL)

# Q2 – View dataframe
print("Q2:\n", df)

# Q3 – Re-read skipping "this row is useless" rows
lines = requests.get(URL).text.splitlines()
skip  = [i for i, l in enumerate(lines) if "this row is useless" in l.lower()]
df    = pd.read_csv(URL, skiprows=skip)
print("Q3:\n", df)

# Q4 – Drop rows with more than 1 NA
df.dropna(thresh=len(df.columns) - 1, inplace=True)

# Q5 – Drop columns where ALL values are NA
df.dropna(axis=1, how='all', inplace=True)

# Q6 – Fill NA in S column
df['S'] = df['S'].fillna(0)

# Q7 – Drop duplicate rows
df.drop_duplicates(inplace=True)

# Q8 – Replace SD0 values <= 0 with NA
df['SD0'] = df['SD0'].where(df['SD0'] > 0, other=np.nan)

# Q9 – Forward fill SD0
df['SD0'] = df['SD0'].ffill()

# Q10 & Q11 – Plot Week vs SD0 with labels
plt.figure(figsize=(8, 5))
plt.plot(df['Week'], df['SD0'], marker='o')
plt.xlabel('Week'); plt.ylabel('SD0 (kg)'); plt.title('Week vs SD0')
plt.tight_layout(); plt.show()

# Q12 – Plot Day vs SD0, SD2, SD1neg
fig, ax = plt.subplots(figsize=(9, 5))
for col, mk in zip(['SD0', 'SD2', 'SD1neg'], ['o', 's', '^']):
    ax.plot(df['Day'], df[col], marker=mk, label=col)
ax.set_xlabel('Day'); ax.set_ylabel('Mass (kg)'); ax.set_title('Day vs SD0, SD2, SD1neg')
ax.legend(); plt.tight_layout()

# Q13 – Save plot
plot_path = 'tutorial2_plot.png'
plt.savefig(plot_path, dpi=150); plt.show()
print("Q13 – Plot saved:", plot_path)

# Q14 – Scale SD0 by 100
df['SD0'] = df['SD0'] * 100

# Q15 – Column headings to title case
df.columns = [c.title() for c in df.columns]

# Q16 – Sort descending by Sd0
df.sort_values('Sd0', ascending=False, inplace=True)

# Q17 – Min, mean, max of S column
s = df['S']
mean_idx = (s - s.mean()).abs().idxmin()
print(f"Q17 – min  of S: {s.min()} at index {s.idxmin()}")
print(f"Q17 – mean of S: {s.mean():.4f} at index {mean_idx}")
print(f"Q17 – max  of S: {s.max()} at index {s.idxmax()}")

# Q18 – Percent change of Sd0 → new column PCSDx
df['PCSDx'] = df['Sd0'].pct_change() * 100

# Q19 – Write to CSV
csv_path = 'tutorial2.csv'
df.to_csv(csv_path, index=False)
print("Q19 – CSV saved:", csv_path)

# Q20 – Confirm files
for p in [plot_path, csv_path]:
    print(f"Q20 – {p} | exists={os.path.exists(p)} | size={os.path.getsize(p)} bytes")

# Q21 – In Jupyter: File → Save and Export As → HTML, then print to PDF in browser