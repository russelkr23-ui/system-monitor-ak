import streamlit as st
import requests
from datetime import datetime

# --- 1. CAPTURE REAL IP ---
def get_real_ip():
    # Streamlit 1.45+ native IP context
    ip = st.context.ip_address
    if not ip or ip.startswith("172.") or ip.startswith("10."):
        # Fallback to Header check if native IP is internal/proxy
        headers = st.context.headers
        ip = headers.get("X-Forwarded-For", "Unknown").split(",")[0].strip()
    return ip

user_ip = get_real_ip()

# --- 2. PERSISTENT MEMORY (Across all users) ---
# We use a global list in 'st.session_state' for the Admin to see
if "master_log" not in st.session_state:
    st.session_state.master_log = []

# Log the current visitor if they aren't already in the list
if user_ip not in [entry['ip'] for entry in st.session_state.master_log] and user_ip != "Unknown":
    entry = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "ip": user_ip,
        "status": "FLAGGED"
    }
    st.session_state.master_log.append(entry)
    # This PRINT makes it show up in the black 'Manage App' logs
    print(f"!!! ENKODER ALERT: Captured {user_ip} !!!")

# --- 3. DASHBOARD UI ---
st.title("🎁 AK GIFTS | SECURITY TERMINAL")
st.error("⚠️ YOUR SCAM HAVE BEEN COMING TO AN END BE SAFE MAN")

st.metric("YOUR DETECTED IP", user_ip)

# --- 4. THE ADMIN VIEW ---
# Add ?admin=true to your URL to see the list
if st.query_params.get("admin") == "true":
    st.divider()
    st.subheader("🕵️ ENKODER MASTER LOGS")
    if st.session_state.master_log:
        st.table(st.session_state.master_log)
    else:
        st.write("No logs captured yet. Try refreshing.")
