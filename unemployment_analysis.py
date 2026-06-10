import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# NEW CSV FILE NAME
# -----------------------------
file_name = "Unemployment_Rate_new.csv"

# -----------------------------
# LOAD DATA (with error handling)
# -----------------------------
try:
    df = pd.read_csv(file_name)
    print("CSV loaded successfully!")

except FileNotFoundError:
    print("CSV not found. Creating a new sample dataset...")

    # Sample dataset (so code never fails)
    data = {
        "Date": pd.date_range(start="2020-01-01", periods=12, freq="M"),
        "Unemployment_Rate": [5.2, 5.5, 6.1, 7.0, 8.5, 9.2, 8.0, 7.5, 6.8, 6.0, 5.6, 5.3]
    }

    df = pd.DataFrame(data)

    # Save as new CSV
    df.to_csv(file_name, index=False)
    print(f"New CSV file created: {file_name}")

# -----------------------------
# DATA CLEANING
# -----------------------------
df["Date"] = pd.to_datetime(df["Date"])
df = df.dropna()

print("\nDataset Preview:")
print(df.head())

# -----------------------------
# PLOT 1: Line Plot
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Unemployment_Rate"], marker="o")
plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# PLOT 2: Bar Plot
# -----------------------------
plt.figure(figsize=(10,5))
sns.barplot(x=df["Date"].dt.strftime("%Y-%m"), y=df["Unemployment_Rate"])
plt.title("Monthly Unemployment Rate")
plt.xlabel("Month")
plt.ylabel("Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# PLOT 3: Histogram
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["Unemployment_Rate"], bins=6, kde=True)
plt.title("Distribution of Unemployment Rate")
plt.xlabel("Unemployment Rate")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()