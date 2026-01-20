import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="AK GIFTS | Internal Security", layout="wide")

# --- 1. CAPTURE REAL IP ---
def get_ip():
    try:
        # 2026 Native method
        ip = st.context.ip_address
        # If it returns a local address, check headers
        if not ip or ip.startswith(("172.", "10.", "127.")):
            headers = st.context.headers
            ip = headers.get("X-Forwarded-For", "Unknown").split(",")[0].strip()
        return ip
    except:
        return "Unknown"

user_ip = get_ip()

# --- 2. PERMANENT LOGGING (Google Form Fix) ---
# Replace this with YOUR actual Form ID (the long string of letters)
FORM_ID = "1FAIpQLSeL-8OqJ1WEUlBsTBcr_LVOJrngK-eHmRsSi7ufcfva10UHcA"
# Replace this with YOUR actual Entry ID
ENTRY_ID = "entry.444157392"

def log_to_google(ip):
    if ip == "Unknown":
        return
    
    url = f"https://docs.google.com/forms/d/e/{FORM_ID}/formResponse"
    # Sending as a data dictionary is MUCH more reliable
    form_data = {ENTRY_ID: ip}
    
    try:
        response = requests.post(url, data=form_data)
        if response.status_code == 200:
            st.session_state["logged"] = True
            print(f"!!! SUCCESS: {ip} added to Google Sheet !!!")
        else:
            print(f"!!! FAILED: Status {response.status_code} !!!")
    except Exception as e:
        print(f"Error: {e}")

if "logged" not in st.session_state:
    log_to_google(user_ip)

# --- 3. UI DASHBOARD ---
st.title("🎁 AK GIFTS | SECURITY TERMINAL")
st.markdown("""
    <style>
    .warning { color: #ff4b4b; font-size: 26px; font-weight: bold; border: 2px dashed red; padding: 20px; text-align: center; }
    </style>
    <div class="warning">⚠️ YOUR SCAM HAVE BEEN COMING TO AN END BE SAFE MAN</div>
    """, unsafe_allow_html=True)

st.divider()
st.metric("YOUR TRACED IP", user_ip)
st.warning("Trace Complete. Metadata Uplink to ENKODER Active.")

# --- 4. ADMIN VIEW ---
if st.query_params.get("admin") == "true":
    st.subheader("🕵️ ENKODER LIVE MONITOR")
    st.info(f"Captured IP: {user_ip}")
    st.write("If you don't see this IP in your Google Sheet, check the 'Logs' in Streamlit.")

