import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="T20 Final Score Predictor",
    page_icon="🏏",
    layout="centered"
)

st.title("🏏 T20 Final Score Predictor")

# ---------------- LOAD MODEL ----------------
with open("rf_score_model.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- LOAD DATA (FOR DROPDOWNS) ----------------
df = pd.read_csv("deliveries_clean.csv")

# Keep original values (IMPORTANT for OneHotEncoder)
batting_teams = sorted(df["batting_team"].dropna().unique())
cities = sorted(df["city"].dropna().unique())

# ---------------- UI INPUTS ----------------
batting_team = st.selectbox(
    "Batting Team",
    batting_teams
)

bowling_team = st.selectbox(
    "Bowling Team",
    [team for team in batting_teams if team != batting_team]
)

city = st.selectbox(
    "City",
    cities
)

st.markdown("---")

current_score = st.number_input(
    "Current Score",
    min_value=0,
    max_value=300,
    value=30,
    step=1
)

balls_left = st.number_input(
    "Balls Left",
    min_value=1,
    max_value=120,
    value=90,
    step=1
)

wickets_left = st.number_input(
    "Wickets Left",
    min_value=0,
    max_value=10,
    value=8,
    step=1
)

# ---------------- FEATURE ENGINEERING ----------------
crr = (current_score * 6) / (120 - balls_left)

# ---------------- PREDICTION ----------------
if st.button("Predict Final Score"):
    input_df = pd.DataFrame({
        "batting_team": [batting_team],
        "bowling_team": [bowling_team],
        "city": [city],
        "current_score": [current_score],
        "balls_left": [balls_left],
        "wickets_left": [wickets_left],
        "crr": [crr]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"🏏 Predicted Final Score: **{round(prediction)}**")
st.write(sorted(df["batting_team"].unique()))
df["batting_team"] = df["batting_team"].str.strip().str.title()
df["bowling_team"] = df["bowling_team"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()

teams = sorted(df["batting_team"].unique())
cities = sorted(df["city"].unique())
