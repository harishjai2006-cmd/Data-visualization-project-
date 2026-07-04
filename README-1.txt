# Data Visualization Project

## Overview

This project focuses on analyzing and visualizing a sales dataset using Python. The main objective is to transform raw data into clear and meaningful visual insights that help understand sales performance, profit trends, regional performance, monthly trends, and category-wise contributions.

The project includes data cleaning, exploratory data analysis, KPI calculation, data visualization, insight generation, and business recommendations.

## Objectives

- Load and explore the sales dataset
- Clean missing and duplicate data
- Analyze sales and profit performance
- Compare sales across different regions
- Identify monthly sales trends
- Analyze category-wise sales and profit
- Study the relationship between sales and profit
- Calculate category sales contribution
- Generate meaningful business insights
- Provide data-driven recommendations

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Python IDLE

## Dataset

The dataset used in this project is:

`Dataset for Data Analytics - Sheet1.csv`

The program automatically detects commonly used columns such as:

- Order Date
- Region
- Category
- Sales
- Profit
- Quantity

## Project Workflow

1. Import required Python libraries
2. Load the CSV dataset
3. Display basic dataset information
4. Detect important columns automatically
5. Check missing values
6. Identify and remove duplicate records
7. Clean and preprocess the dataset
8. Convert date and numerical columns
9. Calculate key performance indicators
10. Create data visualizations
11. Generate insights from the analysis
12. Provide business recommendations

## Data Cleaning

The project performs the following data cleaning operations:

- Removes duplicate rows
- Identifies missing values
- Converts numerical columns into proper numeric format
- Converts the date column into datetime format
- Removes invalid or incomplete important records
- Cleans column names for easier processing

## Key Performance Indicators

The program calculates important KPIs such as:

- Total Sales
- Average Sales
- Total Profit
- Total Quantity Sold
- Best Performing Region
- Peak Sales Month
- Best Sales Category
- Most Profitable Category
- Sales-Profit Correlation

## Visualizations

### 1. Sales by Region

A horizontal bar chart is used to compare total sales across different regions. This visualization helps identify the best-performing and weaker regions.

### 2. Monthly Sales Trend

A line chart displays changes in sales over time. It helps identify sales growth patterns, fluctuations, and the month with the highest sales.

### 3. Sales by Category

A horizontal bar chart compares the sales performance of different product categories and identifies the highest-performing category.

### 4. Profit by Category

A horizontal bar chart compares total profit across product categories and identifies the most profitable category.

### 5. Sales vs Profit

A scatter plot analyzes the relationship between sales and profit. The program also calculates the correlation between these two variables.

### 6. Category Sales Share

A percentage-based horizontal bar chart shows how much each category contributes to total sales.

## Business Insights

The analysis helps identify:

- The region generating the highest total sales
- The month with peak sales performance
- The highest-performing product category
- The most profitable product category
- The relationship between sales and profit
- The contribution of each category to total sales
- Areas where business performance can be improved

## Business Recommendations

Based on the analysis, the following recommendations can be made:

- Apply successful strategies from high-performing regions to weaker regions
- Focus on high-performing product categories
- Investigate the reasons behind low-performing categories
- Expand and protect highly profitable categories
- Study the factors responsible for peak sales periods
- Repeat successful marketing strategies during suitable periods
- Review high-sales but low-profit transactions
- Improve pricing and cost management strategies to increase profit margins

## How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

### Step 2: Install Required Libraries

Open Command Prompt and run:

`pip install pandas numpy matplotlib`

### Step 3: Download the Project Files

Keep the following files in your project folder:

- `data_visualization.py`
- `Dataset for Data Analytics - Sheet1.csv`
- `README.md`

### Step 4: Update the Dataset Path

Make sure the CSV file path in the Python program matches the location of the dataset on your computer.

Example:

`C:\Users\Admin\Downloads\Dataset for Data Analytics - Sheet1.csv`

### Step 5: Run the Program

1. Open `data_visualization.py` in Python IDLE.
2. Click **Run**.
3. Select **Run Module** or press **F5**.
4. View the analysis results in the Python Shell.
5. Close each chart window to display the next visualization.

## Project Structure

Data-Visualization-Project/

- data_visualization.py
- Dataset for Data Analytics - Sheet1.csv
- README.md

## Features

- Automatic column detection
- Data cleaning and preprocessing
- Missing value analysis
- Duplicate data removal
- KPI calculation
- Regional sales analysis
- Monthly trend analysis
- Category performance analysis
- Profit analysis
- Sales and profit correlation analysis
- Category contribution analysis
- Automatic insight generation
- Business recommendations

## Conclusion

This project demonstrates how Python can be used to transform raw sales data into meaningful visual insights. By using data cleaning, data analysis, and visualization techniques, the project identifies important sales patterns, regional performance, category performance, profit trends, and relationships within the dataset.

The insights generated from this project can support better business decisions, improve sales strategies, identify profitable areas, and help organizations understand their overall performance more effectively.

## Author

**HARISH T J**