import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="US Accidents ",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/US_Accidents.csv")
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
    df['Year'] = df['Start_Time'].dt.year
    df['Month'] = df['Start_Time'].dt.month
    df['Hour'] = df['Start_Time'].dt.hour
    df['Day'] = df['Start_Time'].dt.day_name()
    return df

df = load_data()

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Overview", "State Analysis", "Time Analysis", "Weather Analysis"]
)

st.sidebar.markdown("---")

selected_state = st.sidebar.selectbox(
    "Select State",
    sorted(df["State"].dropna().unique())
)

filtered_df = df[df["State"] == selected_state]

st.title("US Accidents Data Dashboard")
st.markdown("Interactive Analysis of Traffic Accidents in the United States")

if page == "Overview":

    st.subheader("Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Accidents", f"{len(df):,}")

    with col2:
        st.metric("Total States", df["State"].nunique())

    with col3:
        st.metric("Most Affected State", df["State"].value_counts().idxmax())

    st.markdown("---")

    st.subheader("Accidents Per Year")

    yearly = df.groupby("Year").size().reset_index(name="Accidents")

    fig = px.line(yearly, x="Year", y="Accidents", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🗺 Accidents by State")

    state_counts = df["State"].value_counts().reset_index()
    state_counts.columns = ["State", "Accidents"]

    fig2 = px.bar(state_counts.head(20),
                  x="State",
                  y="Accidents",
                  title="Top 20 States by Accidents")

    st.plotly_chart(fig2, use_container_width=True)

elif page == "State Analysis":

    st.subheader(f"Analysis for {selected_state}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Accidents", len(filtered_df))

    with col2:
        if not filtered_df.empty:
            st.metric("Highest Severity",
                      filtered_df["Severity"].max())

    st.markdown("---")

    st.subheader("Severity Distribution")

    severity_counts = filtered_df["Severity"].value_counts().reset_index()
    severity_counts.columns = ["Severity", "Count"]

    fig = px.pie(severity_counts,
                 names="Severity",
                 values="Count",
                 hole=0.4)

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Cities in Selected State")

    city_counts = filtered_df["City"].value_counts().head(10).reset_index()
    city_counts.columns = ["City", "Accidents"]

    fig2 = px.bar(city_counts,
                  x="City",
                  y="Accidents")

    st.plotly_chart(fig2, use_container_width=True)

elif page == "Time Analysis":

    st.subheader("Accidents by Hour")

    hourly = df.groupby("Hour").size().reset_index(name="Accidents")

    fig = px.line(hourly, x="Hour", y="Accidents", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Accidents by Day of Week")

    day_order = ["Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday"]

    daily = df["Day"].value_counts().reindex(day_order).reset_index()
    daily.columns = ["Day", "Accidents"]

    fig2 = px.bar(daily, x="Day", y="Accidents")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Accidents by Month")

    monthly = df.groupby("Month").size().reset_index(name="Accidents")

    fig3 = px.line(monthly, x="Month", y="Accidents", markers=True)
    st.plotly_chart(fig3, use_container_width=True)

elif page == "Weather Analysis":

    st.subheader("🌦 Weather Conditions Impact")

    weather_counts = df["Weather_Condition"].value_counts().head(15).reset_index()
    weather_counts.columns = ["Weather", "Accidents"]

    fig = px.bar(weather_counts,
                 x="Weather",
                 y="Accidents")

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🌧 Weather vs Severity")

    weather_severity = df.groupby(["Weather_Condition", "Severity"]).size().reset_index(name="Count")
    weather_severity = weather_severity.sort_values("Count", ascending=False).head(20)

    fig2 = px.bar(weather_severity,
                  x="Weather_Condition",
                  y="Count",
                  color="Severity")

    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
