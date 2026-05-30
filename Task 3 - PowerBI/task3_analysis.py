import pandas as pd

df = pd.read_csv("small_superstore.csv")

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
avg_order_value = total_sales / total_orders
top_region = df.groupby('Region')['Sales'].sum().idxmax()

print("===== KPI VALUES =====")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Average Order Value:", round(avg_order_value, 2))
print("Top Region:", top_region)

customer_sales = df.groupby('Customer Name')['Sales'].sum()

high_value = customer_sales[customer_sales > 3000]
medium_value = customer_sales[(customer_sales >= 1000) & (customer_sales <= 3000)]
low_value = customer_sales[customer_sales < 1000]

print("\n===== CUSTOMER SEGMENTATION =====")
print("High Value Customers:", len(high_value))
print("Medium Value Customers:", len(medium_value))
print("Low Value Customers:", len(low_value))

import matplotlib.pyplot as plt

segments = ['High Value', 'Medium Value', 'Low Value']
counts = [len(high_value), len(medium_value), len(low_value)]

plt.figure(figsize=(6,4))
plt.bar(segments, counts)
plt.title('Customer Segmentation')
plt.ylabel('Number of Customers')
plt.savefig('customer_segmentation.png')
plt.show()