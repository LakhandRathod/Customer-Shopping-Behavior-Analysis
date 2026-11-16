
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Customer Behavior Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- COLORS ----------------
PURPLE = "#800080"
PINK = "#E45DB7"
BLUE = "#1729A5"
LIGHT_BG = "#F8F6FA"

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .stApp {
        background-color: #F8F6FA;
    }

    .main-header {
        background: #E45DB7;
        border: 1px solid #1729A5;
        border-radius: 0px 25px 0px 0px;
        padding: 22px 10px;
        text-align: center;
        margin-bottom: 18px;
    }

    .main-header h1 {
        color: #171717;
        font-size: 40px;
        font-weight: 750;
        margin: 0;
    }

    div[data-testid="stMetric"] {
        background: white;
        border-left: 5px solid #800080;
        border-radius: 6px;
        padding: 22px 12px;
        box-shadow: 0 2px 7px rgba(0,0,0,0.13);
        text-align: center;
    }

    div[data-testid="stMetricLabel"] {
        justify-content: center;
        color: #666;
        font-size: 15px;
    }

    div[data-testid="stMetricValue"] {
        justify-content: center;
        color: #800080;
        font-size: 38px;
        font-weight: 750;
    }

    div[data-testid="stPlotlyChart"] {
        background: white;
        border: 1px solid #D9B5D9;
        border-radius: 16px;
        padding: 8px;
        box-shadow: 0 2px 7px rgba(0,0,0,0.12);
    }

    section[data-testid="stSidebar"] {
        background-color: #FBFAFC;
        border-right: 1px solid #D9B5D9;
    }

    .section-title {
        color: #800080;
        font-size: 17px;
        font-weight: 700;
    }

    #MainMenu, footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    file_path = Path(__file__).parent / "customer.csv"

    if not file_path.exists():
        raise FileNotFoundError(
            "customer.csv file app.py ke same folder mein nahi mili."
        )

    data = pd.read_csv(file_path)

    # Remove extra spaces from column names
    data.columns = data.columns.str.strip()

    return data


try:
    df = load_data()
except Exception as error:
    st.error(f"Dataset load nahi ho paya: {error}")
    st.stop()


# ---------------- COLUMN CHECK ----------------
required_columns = [
    "Customer ID",
    "Age",
    "Gender",
    "Category",
    "Purchase Amount (USD)",
    "Review Rating",
    "Subscription Status",
    "Shipping Type"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    st.error("CSV mein required columns missing hain:")
    st.write(missing_columns)
    st.write("Available columns:", df.columns.tolist())
    st.stop()


# ---------------- DATA CLEANING ----------------
df["Purchase Amount (USD)"] = pd.to_numeric(
    df["Purchase Amount (USD)"], errors="coerce"
)

df["Review Rating"] = pd.to_numeric(
    df["Review Rating"], errors="coerce"
)

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

df = df.dropna(subset=[
    "Customer ID",
    "Purchase Amount (USD)",
    "Age"
])

# Use existing age_group if present; otherwise create it
if "age_group" in df.columns:
    df["Age Group"] = df["age_group"].astype(str)
else:
    df["Age Group"] = pd.cut(
        df["Age"],
        bins=[0, 25, 35, 50, 100],
        labels=[
            "Young Adult",
            "Middle-aged",
            "Adult",
            "Senior"
        ],
        include_lowest=True
    ).astype(str)

age_order = [
    "Young Adult",
    "Middle-aged",
    "Adult",
    "Senior"
]

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.title("Dashboard Filters")
st.sidebar.markdown("---")

def filter_options(column):
    return sorted(df[column].dropna().astype(str).unique().tolist())


subscription_options = filter_options("Subscription Status")
gender_options = filter_options("Gender")
category_options = filter_options("Category")
shipping_options = filter_options("Shipping Type")

selected_subscription = st.sidebar.multiselect(
    "Subscription Status",
    subscription_options,
    default=subscription_options
)

selected_gender = st.sidebar.multiselect(
    "Gender",
    gender_options,
    default=gender_options
)

selected_category = st.sidebar.multiselect(
    "Category",
    category_options,
    default=category_options
)

selected_shipping = st.sidebar.multiselect(
    "Shipping Type",
    shipping_options,
    default=shipping_options
)

if st.sidebar.button("Reset Filters", use_container_width=True):
    st.rerun()


# ---------------- APPLY FILTERS ----------------
filtered_df = df[
    df["Subscription Status"].astype(str).isin(selected_subscription)
    & df["Gender"].astype(str).isin(selected_gender)
    & df["Category"].astype(str).isin(selected_category)
    & df["Shipping Type"].astype(str).isin(selected_shipping)
].copy()


# ---------------- HEADER ----------------
st.markdown("""
<div class="main-header">
    <h1>Customer Behavior Dashboard</h1>
</div>
""", unsafe_allow_html=True)


if filtered_df.empty:
    st.warning("Selected filters ke liye koi customer data available nahi hai.")
    st.stop()


# ---------------- KPI CARDS ----------------
total_customers = filtered_df["Customer ID"].nunique()

average_purchase = filtered_df["Purchase Amount (USD)"].mean()

average_rating = filtered_df["Review Rating"].mean()

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.metric(
        "Number of Customers",
        f"{total_customers / 1000:.1f}K"
        if total_customers >= 1000
        else f"{total_customers:,}"
    )

with kpi2:
    st.metric(
        "Average Purchase Amount",
        f"${average_purchase:.2f}"
    )

with kpi3:
    rating_text = (
        f"{average_rating:.2f}"
        if pd.notna(average_rating)
        else "N/A"
    )
    st.metric("Average of Review Rating", rating_text)


st.write("")


# ---------------- CHART SETTINGS ----------------
chart_layout = dict(
    template="plotly_white",
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=dict(l=15, r=15, t=65, b=30),
    height=280,
    font=dict(family="Arial", size=11, color="#555")
)


# ---------------- ROW 1: THREE CHARTS ----------------
chart1, chart2, chart3 = st.columns([1, 1, 1])


# Subscription Doughnut Chart
with chart1:
    subscription_data = (
        filtered_df.groupby("Subscription Status")
        ["Customer ID"].nunique()
        .reset_index(name="Customers")
    )

    fig_subscription = px.pie(
        subscription_data,
        names="Subscription Status",
        values="Customers",
        hole=0.55,
        title="% of Customers by Subscription Status",
        color_discrete_sequence=[PINK, BLUE]
    )

    fig_subscription.update_traces(
        textposition="outside",
        textinfo="label+percent",
        marker=dict(line=dict(color="white", width=2))
    )

    fig_subscription.update_layout(**chart_layout)
    st.plotly_chart(fig_subscription, use_container_width=True)


# Revenue by Category
with chart2:
    revenue_category = (
        filtered_df.groupby("Category")["Purchase Amount (USD)"]
        .sum()
        .reset_index()
        .sort_values("Purchase Amount (USD)", ascending=False)
    )

    fig_revenue = px.bar(
        revenue_category,
        x="Category",
        y="Purchase Amount (USD)",
        title="Revenue by Category",
        color_discrete_sequence=[BLUE]
    )

    fig_revenue.update_layout(**chart_layout)
    fig_revenue.update_yaxes(title=None)
    fig_revenue.update_xaxes(title=None)
    st.plotly_chart(fig_revenue, use_container_width=True)


# Sales by Category
with chart3:
    sales_category = (
        filtered_df.groupby("Category")["Customer ID"]
        .count()
        .reset_index(name="Sales")
        .sort_values("Sales", ascending=False)
    )

    fig_sales = px.bar(
        sales_category,
        x="Category",
        y="Sales",
        title="Sales by Category",
        color_discrete_sequence=[BLUE]
    )

    fig_sales.update_layout(**chart_layout)
    fig_sales.update_yaxes(title=None)
    fig_sales.update_xaxes(title=None)
    st.plotly_chart(fig_sales, use_container_width=True)


# ---------------- ROW 2: AGE GROUP CHARTS ----------------
st.write("")

age1, age2 = st.columns(2)


# Revenue by Age Group
with age1:
    revenue_age = (
        filtered_df.groupby("Age Group", observed=False)
        ["Purchase Amount (USD)"]
        .sum()
        .reset_index()
    )

    revenue_age["Age Group"] = revenue_age["Age Group"].astype(str)

    revenue_age["sort_order"] = revenue_age["Age Group"].apply(
        lambda x: age_order.index(x) if x in age_order else 99
    )

    revenue_age = revenue_age.sort_values("sort_order")

    fig_age_revenue = px.bar(
        revenue_age,
        x="Purchase Amount (USD)",
        y="Age Group",
        orientation="h",
        title="Revenue by Age Group",
        color_discrete_sequence=[BLUE]
    )

    fig_age_revenue.update_layout(
        **{**chart_layout, "height": 300},
        yaxis=dict(categoryorder="array", categoryarray=age_order[::-1])
    )
    fig_age_revenue.update_xaxes(title=None)
    fig_age_revenue.update_yaxes(title=None)

    st.plotly_chart(fig_age_revenue, use_container_width=True)


# Sales by Age Group
with age2:
    sales_age = (
        filtered_df.groupby("Age Group", observed=False)
        ["Customer ID"]
        .count()
        .reset_index(name="Sales")
    )

    sales_age["Age Group"] = sales_age["Age Group"].astype(str)

    fig_age_sales = px.bar(
        sales_age,
        x="Sales",
        y="Age Group",
        orientation="h",
        title="Sales by Age Group",
        color_discrete_sequence=[BLUE]
    )

    fig_age_sales.update_layout(
        **{**chart_layout, "height": 300},
        yaxis=dict(categoryorder="array", categoryarray=age_order[::-1])
    )
    fig_age_sales.update_xaxes(title=None)
    fig_age_sales.update_yaxes(title=None)

    st.plotly_chart(fig_age_sales, use_container_width=True)


# ---------------- DATA TABLE ----------------
with st.expander("View Customer Records"):
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

st.caption("Customer Shopping Behavior Analysis | Interactive Streamlit Dashboard")

