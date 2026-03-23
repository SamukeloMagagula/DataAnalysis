import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

# URL of the CSV file (example: sample stock data)
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"

try:
    # Step 1: Download the CSV data
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise error for bad status codes

    # Step 2: Convert the text data into a pandas DataFrame
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)

    # Step 3: Display first few rows for verification
    print("Data preview:")
    print(df.head())

    # Step 4: Plot example (assuming numeric columns exist)
    # Here we plot 'Height(Inches)' vs 'Weight(Pounds)' if available
    if 'Height(Inches)' in df.columns and 'Weight(Pounds)' in df.columns:
        plt.figure(figsize=(8, 5))
        plt.scatter(df['Height(Inches)'], df['Weight(Pounds)'], color='blue', alpha=0.6)
        plt.title("Height vs Weight")
        plt.xlabel("Height (inches)")
        plt.ylabel("Weight (pounds)")
        plt.grid(True)
        plt.show()
    else:
        print("Required columns not found in the dataset.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from URL: {e}")
except pd.errors.ParserError as e:
    print(f"Error parsing CSV data: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

