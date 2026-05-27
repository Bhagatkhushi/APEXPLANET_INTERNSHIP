import pandas as pd

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("small_superstore.csv")

print("\n========== DATASET PREVIEW ==========")
print(df.head())

# ==============================
# Dataset Information
# ==============================
print("\n========== DATASET INFORMATION ==========")
print(df.info())

# ==============================
# Statistical Summary
# ==============================
print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# ==============================
# Missing Value Analysis
# ==============================
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# ==============================
# Duplicate Value Analysis
# ==============================
duplicate_count = df.duplicated().sum()

print("\n========== DUPLICATE RECORDS ==========")
print(f"Total Duplicate Rows: {duplicate_count}")

# Remove duplicate records
df = df.drop_duplicates()

# ==============================
# Remove Unnecessary Columns
# ==============================
columns_to_remove = ['Row ID', 'Postal Code']

df.drop(columns=columns_to_remove,
        errors='ignore',
        inplace=True)

# ==============================
# Save Cleaned Dataset
# ==============================
output_file = "Cleaned_Superstore_Data.csv"

df.to_csv(output_file, index=False)

# ==============================
# Final Output Message
# ==============================
print("\n========== DATA CLEANING COMPLETED ==========")
print(f"Cleaned dataset saved successfully as: {output_file}")