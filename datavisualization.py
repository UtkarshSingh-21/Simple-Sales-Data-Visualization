import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sales data (replace 'sales_data.csv' with your actual file)
df = pd.read_csv("sales_data.csv")

# Ensure date column is in datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Extract year and month for trend analysis
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# Aggregate revenue by month
monthly_revenue = df.groupby(["Year", "Month"])["Revenue"].sum().reset_index()

# Plot monthly revenue trends
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_revenue, x="Month", y="Revenue", hue="Year", marker="o")
plt.title("Monthly Revenue Trends")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid()
plt.show()

# Aggregate product demand
product_demand = df.groupby("Product")["Quantity"].sum().reset_index()

# Plot product demand
plt.figure(figsize=(10, 5))
sns.barplot(data=product_demand, x="Product", y="Quantity", palette="viridis")
plt.xticks(rotation=45)
plt.title("Product Demand")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.show()

# Seasonal sales trend (assuming a 'Season' column exists or inferred from months)
df["Season"] = df["Month"].map({12: "Winter", 1: "Winter", 2: "Winter",
                                3: "Spring", 4: "Spring", 5: "Spring",
                                6: "Summer", 7: "Summer", 8: "Summer",
                                9: "Fall", 10: "Fall", 11: "Fall"})

seasonal_sales = df.groupby("Season")["Revenue"].sum().reset_index()

# Plot seasonal sales trends
plt.figure(figsize=(8, 5))
sns.barplot(data=seasonal_sales, x="Season", y="Revenue", palette="coolwarm")
plt.title("Seasonal Sales Trends")
plt.xlabel("Season")
plt.ylabel("Revenue")
plt.show()
