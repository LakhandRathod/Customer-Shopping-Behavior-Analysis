# 📊 Customer Shopping Behavior Analysis

## 📌 Project Overview

This project focuses on analyzing customer shopping behavior to identify purchasing patterns, customer preferences, sales trends, and business insights.

The project follows an end-to-end Data Analytics workflow, starting from dataset loading and data cleaning in Python to Exploratory Data Analysis (EDA), SQL-based analysis, and interactive dashboard development using Power BI.

The final insights are presented through a detailed analytical report and a presentation created using Gamma.

## 🎯 Project Objectives

- Analyze customer purchasing patterns and shopping trends.
- Identify popular product categories and customer preferences.
- Perform data cleaning and preprocessing.
- Explore data using Python and SQL queries.
- Build an interactive Power BI dashboard.
- Generate meaningful business insights to support decision-making.

## 📂 Dataset

The project uses a customer shopping behavior dataset containing information related to customer demographics, purchasing activities, product categories, payment methods, discounts, and shopping preferences.

**Dataset includes:**
- Customer ID
- Age and Gender
- Item Purchased
- Category
- Purchase Amount
- Location
- Season
- Payment Method
- Discount Applied
- Review Rating
- Subscription Status

*Note: Actual columns depend on the dataset used in the project.*

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data analysis and preprocessing |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| SQL | Data querying and analysis |
| MySQL / PostgreSQL / SQL Server | Database management |
| Power BI | Interactive dashboard |
| Gamma AI | Project presentation |
| Jupyter Notebook | Python development |
| Git & GitHub | Version control |

## 🔄 Project Workflow

### 1. Data Loading
- Imported the dataset into Python.
- Used Pandas to load and inspect the data.
- Checked dataset dimensions, columns, and data types.

### 2. Exploratory Data Analysis (EDA)
- Analyzed customer demographics.
- Explored purchasing trends.
- Identified popular product categories.
- Examined payment methods and customer preferences.
- Created visualizations to understand patterns.

### 3. Data Cleaning & Preprocessing
- Checked for missing values.
- Identified and handled duplicate records.
- Corrected data types.
- Standardized column names and values.
- Prepared clean data for further analysis.

### 4. SQL Analysis
- Imported cleaned data into the SQL database.
- Performed aggregation and filtering.
- Used GROUP BY, ORDER BY, JOIN, and subqueries.
- Analyzed sales, customer behavior, and product performance.
- Extracted meaningful business insights.

### 5. Power BI Dashboard
- Connected the cleaned dataset to Power BI.
- Created interactive visualizations.
- Developed KPI cards and charts.
- Added slicers and filters.
- Designed a dashboard to communicate key business insights.

### 6. Report & Presentation
- Prepared a project report containing methodology, analysis, and findings.
- Created a professional presentation using Gamma AI.
- Summarized key insights and business recommendations.

## 📊 Dashboard

The Power BI dashboard provides an interactive view of customer shopping behavior.

**Key Dashboard Metrics:**
- Total Revenue
- Total Customers
- Average Purchase Amount
- Average Review Rating
- Sales by Product Category
- Customer Distribution by Gender
- Payment Method Analysis
- Seasonal Shopping Trends
- Subscription Analysis

*Add your Power BI dashboard screenshots here.*

![Dashboard Preview](images/dashboard.png)

## 📈 Key Results & Business Insights

The analysis aims to identify:

- Customer purchasing preferences and spending patterns.
- Best-performing product categories.
- Revenue distribution across different customer segments.
- Popular payment methods.
- Seasonal purchasing behavior.
- Differences between subscribed and non-subscribed customers.

These insights can help businesses improve marketing strategies, customer engagement, product planning, and sales performance.

## 📁 Project Structure

```text
Customer-Shopping-Behavior-Analysis/
│
├── dataset/
│   └── customer_shopping_behavior.csv
│
├── notebooks/
│   └── customer_behavior_analysis.ipynb
│
├── sql/
│   └── customer_analysis.sql
│
├── dashboard/
│   ├── customer_behavior_dashboard.pbix
│   └── dashboard.png
│
├── reports/
│   └── project_report.pdf
│
├── presentation/
│   └── project_presentation.pdf
│
├── requirements.txt
└── README.md
```

## ⚙️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd Customer-Shopping-Behavior-Analysis
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Python Notebook

```bash
jupyter notebook
```

Open the notebook inside the `notebooks/` folder and execute the cells.

### Step 5: Run SQL Queries

- Open MySQL Workbench, PostgreSQL, or SQL Server Management Studio.
- Connect to your database.
- Import the cleaned dataset.
- Execute the SQL scripts from the `sql/` folder.

### Step 6: Open Power BI Dashboard

Open the `.pbix` file from the `dashboard/` folder using Power BI Desktop.

## 📦 Requirements

Create a `requirements.txt` file with:

```text
pandas
numpy
matplotlib
seaborn
jupyter
sqlalchemy
pymysql
psycopg2-binary
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

## 🚀 Future Improvements

- Develop a live interactive dashboard using Streamlit.
- Automate data cleaning and reporting.
- Integrate real-time data sources.
- Implement advanced customer segmentation.
- Apply machine learning for customer purchase prediction.

## 👨‍💻 Author

**Lakhan Rathod**

Computer Engineering Student | Aspiring Data Analyst

**Technical Skills:** Python | SQL | Power BI | Excel | Pandas | NumPy | Data Visualization

- GitHub: https://github.com/callmelucky
- Portfolio: https://lakhan-rathod-portfolio.netlify.app

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

*This project demonstrates an end-to-end data analytics workflow, combining Python, SQL, and Power BI to transform raw customer data into meaningful business insights.*