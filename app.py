import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page Config for a Pro-Security Look
st.set_page_config(page_title="AK GIFTS | Internal Security", page_icon="🔒", layout="wide")

# 2. IP CAPTURE LOGIC (Silent)
def log_visitor(ip):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} - IP: {ip}\n")

headers = st.context.headers
user_ip = headers.get("X-Forwarded-For", "127.0.0.1")
log_visitor(user_ip) # This saves the IP to your server automatically

# 3. Custom CSS for the Footer and Warning Glow
st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .warning-text { color: #ff4b4b; font-weight: bold; font-size: 24px; text-shadow: 0 0 10px #ff4b4b; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; color: #555; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 4. Header & Branding
st.title("🛡️ AK GIFTS: SYSTEM MONITOR")
st.write(f"**Authorized Access Only** | Session ID: {hash(user_ip)}")
st.divider()

# 5. The Intimidating Message
st.markdown('<p class="warning-text">⚠️ SECURITY ALERT: YOUR SCAM HAVE BEEN COMING TO AN END BE SAFE MAN</p>', unsafe_allow_html=True)
st.error("Trace Protocol 09: SYSTEM COMPROMISED. Location Uplink Active.")

# 6. Dashboard Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📍 Target Metadata")
    st.info(f"**Assigned IP:** {user_ip}")
    st.info(f"**Status:** Under Surveillance")
    st.warning("Contact Aleena soon THE ONE WHO SCAMMED Rs: 1500.")

with col2:
    st.subheader("📊 Live Trace Activity")
    # Fake progress bars to simulate a "hack"
    st.write("Extracting local network data...")
    st.progress(85)
    st.write("Bypassing proxy layers...")
    st.progress(40)
    
    # Mock log table
    data = {
        "Timestamp": [datetime.now().strftime("%H:%M:%S"), "14:10:02", "14:09:55"],
        "Action": ["IP_LOGGED", "FIREWALL_BREACH", "UPLINK_ESTABLISHED"],
        "Source": [user_ip, "ENKODER_MAIN", "AK_SERVER_01"]
    }
    st.table(pd.DataFrame(data))

# 7. Copyright Footer
st.markdown('<div class="footer">MADE BY ENKODER.</div>', unsafe_allow_html=True)