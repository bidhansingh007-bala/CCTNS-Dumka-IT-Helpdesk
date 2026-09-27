import streamlit as st
import requests

# Page ki setting (Tab ka naam aur icon)
st.set_page_config(
    page_title="CCTNS Dumka IT Helpdesk",
    page_icon="🖥️",
    layout="centered"
)

st.title("🖥️ CCTNS Dumka IT Helpdesk")
st.markdown("---")

st.header("Symptoms")
st.write("System में जो problem है, उसे select करें:")

# 2 Columns mein checkboxes
col1, col2 = st.columns(2)

with col1:
    power = st.checkbox("1. CPU Power ON नहीं हो रहा?")
    display = st.checkbox("2. Display नहीं आ रहा?")
    os_loading = st.checkbox("3. OS Loading नहीं हो रहा?")
    keyboard = st.checkbox("4. Keyboard काम नहीं कर रहा?")
    mouse = st.checkbox("5. Mouse काम नहीं कर रहा?")

with col2:
    beep = st.checkbox("6. Beep Sound आ रहा है?")
    time_change = st.checkbox("7. Time automatically change हो रहा है?")
    usb = st.checkbox("8. USB Port काम नहीं कर रहा?")
    shutdown = st.checkbox("9. Computer automatically shutdown हो रहा है?")

st.markdown("---")

if st.button("🔍 Diagnose Problem", use_container_width=True):

    # UI ke inputs ko API ke format mein badalna
    payload = {
        "power_on": 0 if power else 1,
        "display_on": 0 if display else 1,
        "os_loading": 0 if os_loading else 1,
        "key_board": 0 if keyboard else 1,
        "mouse": 0 if mouse else 1,
        "beep_sound": 1 if beep else 0,
        "time_automatic_change": 1 if time_change else 0,
        "USB_port_not_working": 1 if usb else 0,
        "automatic_shut_down": 1 if shutdown else 0
    }

    try:
        # Live Render API URL
        response = requests.post("https://cctns-dumka-it-helpdesk.onrender.com/diagnose", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            
            # Agar illogical input (jaise bina power ke display) ka error aaye
            if "Error" in result:
                st.error(f"⚠️ {result['Error']}")
            else:
                # --- DARK AUR BOLD UI DESIGN ---
                st.markdown(f"""
                <div style="background-color: #1E1E1E; padding: 25px; border-radius: 10px; border: 2px solid #4CAF50; box-shadow: 2px 2px 15px rgba(0,0,0,0.5);">
                    <h2 style="color: #4CAF50; margin-top: 0px;">🛠️ Solution (उपाय):</h2>
                    <p style="color: #FFFFFF; font-size: 24px; font-weight: 900; line-height: 1.4;">{result['Solution_Advice']}</p>
                    <hr style="border: 1px solid #444444; margin: 20px 0;">
                    <h4 style="color: #FFA500; margin-bottom: 5px;">⚠️ Problem: <span style="color: #FFFFFF; font-weight: bold;">{result['Problem_Kha_Hai']}</span></h4>
                    <h4 style="color: #00BFFF; margin-top: 0px;">🤖 AI Confidence: <span style="color: #FFFFFF; font-weight: bold;">{result['AI_Ki_Guarantee_Sambhawana']}</span></h4>
                </div>
                """, unsafe_allow_html=True)
                # -------------------------------
                
        else:
            st.error(f"API Error (Status Code: {response.status_code})")

    except requests.exceptions.ConnectionError:
        st.error("FastAPI server (Render) से connect नहीं हो पाया।")