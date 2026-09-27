import streamlit as st
import requests
import os

# Page ki setting
st.set_page_config(
    page_title="CCTNS Dumka IT Helpdesk",
    page_icon="🖥️",
    layout="centered"
)

# --- CUSTOM CSS FOR LIGHT THEME ---
st.markdown("""
<style>
/* Background ko light-grey/white karna */
.stApp {
    background-color: #F4F6F9 !important;
}
/* Saare text ko dark (black/grey) karna taaki light background par dikhe */
.stApp, h1, h2, h3, h4, p, label {
    color: #1E1E1E !important;
}
/* Checkbox text */
div[data-testid="stCheckbox"] label p {
    font-size: 19px !important;
    font-weight: 600 !important;
    color: #2C3E50 !important;
}
</style>
""", unsafe_allow_html=True)
# -----------------------------------

# --- LOGO DISPLAY LOGIC ---
if os.path.exists("logo.jpeg"):
    st.image("logo.jpeg", use_container_width=True)
elif os.path.exists("logo.jpg"):
    st.image("logo.jpg", use_container_width=True)
elif os.path.exists("logo.png"):
    st.image("logo.png", use_container_width=True)
else:
    st.warning("⚠️ Logo nahi dikh raha kyunki GitHub par file ka naam 'logo.jpg' ya 'logo.jpeg' nahi hai.")
    st.title("🖥️ CCTNS Dumka IT Helpdesk")
# --------------------------
    
st.markdown("---")

st.header("Symptoms")
st.write("System में जो problem है, उसे select करें:")

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
    
    # --- SMART VALIDATION ---
    if not (power or display or os_loading or keyboard or mouse or beep or time_change or usb or shutdown):
        st.warning("⚠️ सिस्टम एकदम ठीक लग रहा है! कृपया Diagnose करने से पहले कम से कम एक Problem (Symptom) सेलेक्ट करें।")
    else:
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
            response = requests.post("https://cctns-dumka-it-helpdesk.onrender.com/diagnose", json=payload)
            
            if response.status_code == 200:
                result = response.json()
                
                if "Error" in result:
                    st.error(f"⚠️ {result['Error']}")
                else:
                    primary_problem = result['Problem_Kha_Hai']
                    primary_solution = result['Solution_Advice']
                    
                    extra_solutions = ""
                    if keyboard and "Keyboard" not in primary_problem:
                        extra_solutions += "<li style='margin-bottom: 8px;'><b>Keyboard:</b> USB cable निकालकर दूसरे Port में लगायें या कीबोर्ड बदलें।</li>"
                    if mouse and "Mouse" not in primary_problem:
                        extra_solutions += "<li style='margin-bottom: 8px;'><b>Mouse:</b> नीचे का सेंसर साफ करें या दूसरे Port में लगाकर चेक करें।</li>"
                    if time_change and "CMOS" not in primary_problem:
                        extra_solutions += "<li style='margin-bottom: 8px;'><b>Date/Time:</b> Motherboard की CMOS Battery (CR2032) खत्म हो गई है, उसे बदलें।</li>"
                    if usb and "USB" not in primary_problem:
                        extra_solutions += "<li style='margin-bottom: 8px;'><b>USB Port:</b> BIOS settings चेक करें या Motherboard का USB Driver अपडेट करें।</li>"
                    if shutdown and "Overheating" not in primary_problem:
                        extra_solutions += "<li style='margin-bottom: 8px;'><b>Auto Shutdown:</b> CPU Fan चेक करें (Overheating हो सकती है) और Thermal Paste लगायें।</li>"
                    if beep and "RAM" not in primary_problem:
                        extra_solutions += "<li style='margin-bottom: 8px;'><b>Beep Sound:</b> RAM निकालकर रबर से साफ करें और वापस लगायें।</li>"
                    
                    extra_html = ""
                    if extra_solutions != "":
                        extra_html = f'<hr style="border: 1px dashed #AAAAAA; margin: 20px 0;"><h4 style="color: #D35400; margin-bottom: 12px; margin-top: 0px;">📌 अन्य चुनी गई समस्याओं के उपाय:</h4><ul style="color: #333333; font-size: 20px; line-height: 1.4;">{extra_solutions}</ul>'
                    
                    # Yahan spacing remove kar di gayi hai taaki code block na bane
                    html_ui = f"""<div style="background-color: #FFFFFF; padding: 25px; border-radius: 12px; border: 2px solid #27AE60; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);">
<h3 style="color: #27AE60; margin-top: 0px; margin-bottom: 10px;">🛠️ Main Solution (मुख्य उपाय):</h3>
<p style="color: #111111; font-size: 26px; font-weight: 900; line-height: 1.4; margin-bottom: 5px;">{primary_solution}</p>
{extra_html}
<hr style="border: 1px solid #DDDDDD; margin: 20px 0;">
<div style="background-color: #F8F9F9; padding: 15px; border-radius: 8px; border: 1px solid #EEEEEE;">
<h4 style="color: #C0392B; margin: 0px 0px 8px 0px;">⚠️ Main Root Cause: <span style="color: #222222; font-weight: bold;">{primary_problem}</span></h4>
<h4 style="color: #2980B9; margin: 0px;">🤖 AI Confidence: <span style="color: #222222; font-weight: bold;">{result['AI_Ki_Guarantee_Sambhawana']}</span></h4>
</div>
</div>"""
                    st.markdown(html_ui, unsafe_allow_html=True)
                    
            else:
                st.error(f"API Error (Status Code: {response.status_code})")

        except requests.exceptions.ConnectionError:
            st.error("FastAPI server (Render) से connect नहीं हो पाया।")

# --- FOOTER AUR DISCLAIMER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #555555; padding: 15px; border-top: 1px solid #DDDDDD; margin-top: 20px;">
    <h4 style="margin: 0px; color: #27AE60; letter-spacing: 1px;">For IT Helpdesk Support - Dumka District</h4>
    <p style="margin-top: 5px; font-size: 13px; font-style: italic;">⚠️ Disclaimer: Ye AI Assistant hai, official CCTNS data se connected nahi</p>
</div>
""", unsafe_allow_html=True)