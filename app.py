import streamlit as st
import requests
from datetime import datetime
import pandas as pd

# --- CONFIG ---
st.set_page_config(page_title="AK GIFTS | Internal Security", layout="wide")
# PASTE YOUR GOOGLE SHEET URL BELOW
SHEET_URL = "https://docs.google.com/spreadsheets/d/1gjtKh6-wN_gvGZ7i9YWpAETE4bqnfqyX1kfAHlIyi1s/edit?usp=sharing"

# --- 1. CAPTURE REAL IP ---
def get_ip():
    headers = st.context.headers
    ip = headers.get("X-Forwarded-For", "Unknown").split(",")[0].strip()
    return ip

user_ip = get_ip()

# --- 2. SEND TO GOOGLE SHEETS (Permanent Storage) ---
# This happens silently in the background
if user_ip != "Unknown" and "logged" not in st.session_state:
    try:
        # We use a simple trick to log via a Google Form or Apps Script, 
        # but for now, we'll log it to the Streamlit Cloud Logs as a backup
        print(f"CRITICAL DATA: {datetime.now()} | {user_ip}")
        st.session_state["logged"] = True
    except:
        pass

# --- 3. UI DASHBOARD ---
st.title("🎁 AK GIFTS | SECURITY TERMINAL")
st.markdown("""
    <style>
    .warning { color: #ff4b4b; font-size: 24px; font-weight: bold; border: 2px solid red; padding: 20px; text-align: center; }
    </style>
    <div class="warning">⚠️ YOUR SCAM HAVE BEEN COMING TO AN END BE SAFE MAN</div>
    """, unsafe_allow_html=True)

st.divider()
st.metric("YOUR TRACED IP", user_ip)
st.warning("System Trace Active. Social Security verification pending for 'Aleena'.")

# --- 4. ADMIN VIEW (Reading from the logs) ---
if st.query_params.get("admin") == "true":
    st.subheader("🕵️ ENKODER MASTER LOGS")
    st.write("To see the permanent list, check your **Streamlit Manage App > Logs** console.")
    st.info("Because the cloud deletes files, the only 100% safe way to see their IP is the 'Logs' button in the bottom right.")
