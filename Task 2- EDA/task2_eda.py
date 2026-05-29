import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("small_superstore.csv")

print("\n========== DATASET OVERVIEW ==========")
print(df.head())

print("\n========== DATASET INFO ==========")
print(df.info())

print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe())

# Category Analysis
print("\n========== CATEGORY COUNT ==========")
print(df['Category'].value_counts())

# Region Analysis
print("\n========== REGION COUNT ==========")
print(df['Region'].value_counts())

# Top 5 Products by Sales
print("\n========== TOP 5 PRODUCTS BY SALES ==========")
print(
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Top 5 Customers by Sales
print("\n========== TOP 5 CUSTOMERS BY SALES ==========")
print(
    df.groupby('Customer Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Profit by Category
print("\n========== PROFIT BY CATEGORY ==========")
print(
    df.groupby('Category')['Profit']
    .sum()
    .sort_values(ascending=False)
)

# Correlation Matrix
print("\n========== CORRELATION MATRIX ==========")
print(df[['Sales', 'Profit', 'Quantity', 'Discount']].corr())

# -------------------------
# VISUALIZATIONS
# -------------------------

# Sales Distribution
plt.figure(figsize=(8,5))
df['Sales'].hist(bins=20)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("sales_distribution.png")
plt.show()

# Sales by Region
plt.figure(figsize=(8,5))
df.groupby('Region')['Sales'].sum().plot(kind='bar')
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.savefig("sales_by_region.png")
plt.show()

# Profit by Category
plt.figure(figsize=(8,5))
df.groupby('Category')['Profit'].sum().plot(kind='bar')
plt.title("Profit by Category")
plt.ylabel("Profit")
plt.savefig("profit_by_category.png")
plt.show()

# Sales vs Profit
plt.figure(figsize=(8,5))
plt.scatter(df['Sales'], df['Profit'])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.savefig("sales_vs_profit.png")
plt.show()

# Top 10 Products by Sales

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_products.plot(kind='bar')
print(top_products)

plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# =========================
# Business Questions
# =========================

print("\n===== BUSINESS INSIGHTS =====")

print("\nQ1. What are the Top 5 Products by Sales?")
print(df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5))

print("\nQ2. Which Region Generates the Highest Sales?")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

print("\nQ3. Which Category Generates the Highest Profit?")
print(df.groupby('Category')['Profit'].sum().sort_values(ascending=False))

print("\nQ4. Who are the Top 5 Customers by Sales?")
print(df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5))

print("\nQ5. What is the Average Sales Value?")
print(df['Sales'].mean())

print("\nKPI Values")
print("Total Sales =", df['Sales'].sum())
print("Total Profit =", df['Profit'].sum())
print("Total Orders =", df['Order ID'].nunique())
print("Top Region =", df.groupby('Region')['Sales'].sum().idxmax())
print("\nTask 2 Completed Successfully!")
