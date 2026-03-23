import numpy as np
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file into a DataFrame
n df = pd.read_excel("wfa_girls_0-to-13-weeks_zscores.xlsx")
# Look at the top and bottom 5 rows of the data using head() and tail().

# Display the first five rows
df.head(5)

# Display the last few rows
df.tail(5)
# Plot Week vs SD0
plt.figure()
plt.plot(df['Week'], df['SD0'])
# Plot Week vs SD0
plt.figure()
plt.plot(df['Week'], df['SD0'])

# Add labels and title
plt.xlabel('Week')
plt.ylabel('SD0')
plt.title('Week vs SD0')

# Show the plot
plt.show()
# Create a Day column from Week
df['Day'] = df['Week'] * 7

# Plot Day vs SD0, SD1, and SD1neg
plt.figure()

plt.plot(df['Day'], df['SD0'], label='SD0')
plt.plot(df['Day'], df['SD1'], label='SD1')
plt.plot(df['Day'], df['SD1neg'], label='SD1neg')

# Labels and title
plt.xlabel('Day')
plt.ylabel('Z-score values')
plt.title('Day vs SD0, SD1, and SD1neg')

plt.legend()
plt.show()

# Create a Day column from Week
df['Day'] = df['Week'] * 7

# Plot Day vs SD0, SD1, and SD1neg
plt.figure()

plt.plot(df['Day'], df['SD0'], label='SD0')
plt.plot(df['Day'], df['SD1'], label='SD1')
plt.plot(df['Day'], df['SD1neg'], label='SD1neg')

# Labels and title
plt.xlabel('Day')
plt.ylabel('Z-score values')
plt.title('Day vs SD0, SD1, and SD1neg')

plt.legend()


# Save the figure
plt.savefig('Z-score values over time.png', dpi=300, bbox_inches='tight')

plt.show()
# I tried to scale SD0, SD1, SD2

# List of SD columns
sd_columns = ['SD0', 'SD1', 'SD2']

# Scale them by 100
df[sd_columns] = df[sd_columns] * 100

# Verify the changes
print(df[sd_columns].head())
# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Verify the changes
print(df.columns)
# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Verify the changes
print(df.columns)

# Minimum value and its index
min_value = df['s'].min()
min_index = df['s'].idxmin()

# Maximum value and its index
max_value = df['s'].max()
max_index = df['s'].idxmax()

# Mean value
mean_value = df['s'].mean()

print("Minimum value:", min_value, "at index:", min_index)
print("Mean value:", mean_value)
print("Maximum value:", max_value, "at index:", max_index)
# Use column is sd0 to calculate the percent change and create a new column called PCSDx
df['PCSDx'] = df['sd0'].pct_change() * 100  # multiply by 100 to get percent
# View the new column
print(df[['sd0', 'PCSDx']].head())
df.to_csv("tutorial2.csv", index=False)
# Load the saved CSV
df_check = pd.read_csv("tutorial2.csv")

# Preview the data
print(df_check.head())

# Check structure
print(df_check.info())