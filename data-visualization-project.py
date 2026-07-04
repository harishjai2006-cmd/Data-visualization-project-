import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings

warnings.filterwarnings("ignore")

file_path = r"C:\Users\Admin\Downloads\Dataset for Data Analytics - Sheet1.csv"

if not os.path.exists(file_path):
    print("File not found.")
    input("Press Enter to exit...")
    exit()

df = pd.read_csv(file_path, encoding_errors="ignore")

print("\nDataset Loaded Successfully")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

df.columns = df.columns.str.strip().str.replace("\n", " ", regex=False)

def find_column(possible_names):
    for actual_column in df.columns:
        clean_actual = actual_column.lower().replace("_", " ").replace("-", " ").strip()

        for possible in possible_names:
            clean_possible = possible.lower().replace("_", " ").replace("-", " ").strip()

            if clean_actual == clean_possible:
                return actual_column

    return None

date_col = find_column([
    "Order Date",
    "Date",
    "Transaction Date",
    "Sales Date"
])

region_col = find_column([
    "Region",
    "State",
    "Country",
    "Market",
    "Location"
])

category_col = find_column([
    "Category",
    "Product Category",
    "Product",
    "Segment"
])

sales_col = find_column([
    "Sales",
    "Revenue",
    "Total Sales",
    "Amount",
    "Sales Amount"
])

profit_col = find_column([
    "Profit",
    "Net Profit",
    "Gross Profit"
])

quantity_col = find_column([
    "Quantity",
    "Qty",
    "Units Sold",
    "Order Quantity"
])

print("\nDetected Columns:")
print("Date:", date_col)
print("Region:", region_col)
print("Category:", category_col)
print("Sales:", sales_col)
print("Profit:", profit_col)
print("Quantity:", quantity_col)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

for column in [sales_col, profit_col, quantity_col]:
    if column is not None:
        df[column] = (
            df[column]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("$", "", regex=False)
            .str.replace("₹", "", regex=False)
            .str.strip()
        )

        df[column] = pd.to_numeric(df[column], errors="coerce")

if date_col is not None:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

important_columns = [
    column
    for column in [date_col, region_col, category_col, sales_col]
    if column is not None
]

if important_columns:
    df = df.dropna(subset=important_columns)

print("\nRows After Cleaning:", len(df))

print("\nSummary Statistics:")
print(df.describe(include="all"))

print("\nKey Performance Indicators:")

if sales_col is not None:
    total_sales = df[sales_col].sum()
    average_sales = df[sales_col].mean()

    print(f"Total Sales: {total_sales:,.2f}")
    print(f"Average Sales: {average_sales:,.2f}")

if profit_col is not None:
    total_profit = df[profit_col].sum()
    print(f"Total Profit: {total_profit:,.2f}")

if quantity_col is not None:
    total_quantity = df[quantity_col].sum()
    print(f"Total Quantity: {total_quantity:,.0f}")

if region_col is not None and sales_col is not None:
    region_sales = df.groupby(region_col)[sales_col].sum().sort_values()

    plt.figure(figsize=(10, 6))

    bars = plt.barh(
        region_sales.index.astype(str),
        region_sales.values
    )

    best_region = region_sales.idxmax()

    plt.title(
        f"{best_region} Generated the Highest Total Sales",
        fontsize=15,
        fontweight="bold"
    )

    plt.xlabel("Total Sales")
    plt.ylabel("Region")

    for bar in bars:
        width = bar.get_width()

        plt.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f" {width:,.0f}",
            va="center"
        )

    plt.tight_layout()
    plt.show()

    print(
        f"\nInsight: {best_region} is the strongest sales region "
        f"with total sales of {region_sales.max():,.2f}."
    )

if date_col is not None and sales_col is not None:
    monthly_data = df.dropna(subset=[date_col]).copy()

    monthly_data["Month"] = (
        monthly_data[date_col]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_sales = monthly_data.groupby("Month")[sales_col].sum()

    plt.figure(figsize=(12, 6))

    plt.plot(
        monthly_sales.index,
        monthly_sales.values,
        marker="o"
    )

    peak_month = monthly_sales.idxmax()
    peak_value = monthly_sales.max()

    plt.title(
        f"Sales Peaked in {peak_month}",
        fontsize=15,
        fontweight="bold"
    )

    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

    print(
        f"\nInsight: The highest monthly sales occurred in "
        f"{peak_month}, reaching {peak_value:,.2f}."
    )

if category_col is not None and sales_col is not None:
    category_sales = df.groupby(category_col)[sales_col].sum().sort_values()

    plt.figure(figsize=(10, 6))

    bars = plt.barh(
        category_sales.index.astype(str),
        category_sales.values
    )

    best_category = category_sales.idxmax()

    plt.title(
        f"{best_category} Leads Category Sales",
        fontsize=15,
        fontweight="bold"
    )

    plt.xlabel("Total Sales")
    plt.ylabel("Category")

    for bar in bars:
        width = bar.get_width()

        plt.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f" {width:,.0f}",
            va="center"
        )

    plt.tight_layout()
    plt.show()

    print(
        f"\nInsight: {best_category} is the top-performing category "
        f"with sales of {category_sales.max():,.2f}."
    )

if category_col is not None and profit_col is not None:
    category_profit = df.groupby(category_col)[profit_col].sum().sort_values()

    plt.figure(figsize=(10, 6))

    bars = plt.barh(
        category_profit.index.astype(str),
        category_profit.values
    )

    best_profit_category = category_profit.idxmax()

    plt.title(
        f"{best_profit_category} Generates the Highest Profit",
        fontsize=15,
        fontweight="bold"
    )

    plt.xlabel("Total Profit")
    plt.ylabel("Category")

    for bar in bars:
        width = bar.get_width()

        plt.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f" {width:,.0f}",
            va="center"
        )

    plt.tight_layout()
    plt.show()

    print(
        f"\nInsight: {best_profit_category} contributes the highest "
        f"profit of {category_profit.max():,.2f}."
    )

if sales_col is not None and profit_col is not None:
    scatter_data = df[[sales_col, profit_col]].dropna()

    plt.figure(figsize=(10, 6))

    plt.scatter(
        scatter_data[sales_col],
        scatter_data[profit_col],
        alpha=0.6
    )

    plt.axhline(y=0, linewidth=1)

    plt.title(
        "Relationship Between Sales and Profit",
        fontsize=15,
        fontweight="bold"
    )

    plt.xlabel("Sales")
    plt.ylabel("Profit")

    plt.tight_layout()
    plt.show()

    correlation = scatter_data[[sales_col, profit_col]].corr().iloc[0, 1]

    print(
        f"\nInsight: The correlation between sales and profit is "
        f"{correlation:.2f}."
    )

if category_col is not None and sales_col is not None:
    category_share = df.groupby(category_col)[sales_col].sum().sort_values()

    percentage_share = (
        category_share / category_share.sum()
    ) * 100

    plt.figure(figsize=(10, 6))

    bars = plt.barh(
        percentage_share.index.astype(str),
        percentage_share.values
    )

    largest_share_category = percentage_share.idxmax()

    plt.title(
        f"{largest_share_category} Holds the Largest Sales Share",
        fontsize=15,
        fontweight="bold"
    )

    plt.xlabel("Share of Total Sales (%)")
    plt.ylabel("Category")

    for bar in bars:
        value = bar.get_width()

        plt.text(
            value,
            bar.get_y() + bar.get_height() / 2,
            f" {value:.1f}%",
            va="center"
        )

    plt.tight_layout()
    plt.show()

print("\nFinal Project Insights:")

number = 1

if region_col is not None and sales_col is not None:
    print(
        f"{number}. Best Region: {region_sales.idxmax()} "
        f"with {region_sales.max():,.2f} in sales."
    )
    number += 1

if date_col is not None and sales_col is not None:
    print(
        f"{number}. Peak Sales Month: {monthly_sales.idxmax()} "
        f"with {monthly_sales.max():,.2f} in sales."
    )
    number += 1

if category_col is not None and sales_col is not None:
    print(
        f"{number}. Best Sales Category: {category_sales.idxmax()} "
        f"with {category_sales.max():,.2f} in sales."
    )
    number += 1

if category_col is not None and profit_col is not None:
    print(
        f"{number}. Most Profitable Category: "
        f"{category_profit.idxmax()} with "
        f"{category_profit.max():,.2f} in profit."
    )
    number += 1

if sales_col is not None and profit_col is not None:
    print(
        f"{number}. Sales-Profit Correlation: {correlation:.2f}."
    )

print("\nBusiness Recommendations:")

if region_col is not None and sales_col is not None:
    print(
        f"1. Apply successful strategies from "
        f"{region_sales.idxmax()} to weaker regions."
    )

if category_col is not None and sales_col is not None:
    print(
        f"2. Focus on the strong performance of "
        f"{category_sales.idxmax()} while improving weaker categories."
    )

if category_col is not None and profit_col is not None:
    print(
        f"3. Expand the profitability of "
        f"{category_profit.idxmax()}."
    )

if date_col is not None and sales_col is not None:
    print(
        f"4. Study the factors behind the sales peak in "
        f"{monthly_sales.idxmax()}."
    )

if sales_col is not None and profit_col is not None:
    print(
        "5. Review high-sales but low-profit transactions "
        "to improve profit margins."
    )

print("\nProject Completed Successfully")

input("\nPress Enter to close...")
