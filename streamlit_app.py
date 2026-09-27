import streamlit as st
import requests

st.set_page_config(
    page_title="CCTNS Dumka IT Helpdesk",
    page_icon="🖥️",
    layout="centered"
)

st.title("🖥️ CCTNS Dumka IT Helpdesk")
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
    motherboard = st.checkbox("10. Motherboard problem है?")

st.markdown("---")

if st.button("🔍 Diagnose Problem", use_container_width=True):

    data = {
        "power_on": 0 if power else 1,
        "display_on": 0 if display else 1,
        "os_loading": 0 if os_loading else 1,
        "key_board": 0 if keyboard else 1,
        "mouse": 0 if mouse else 1,
        "beep_sound": 1 if beep else 0,
        "time_automatic_change": 1 if time_change else 0,
        "USB_port_not_working": 1 if usb else 0,
        "automatic_shut_down": 1 if shutdown else 0,
        "motherboard_problem": 1 if motherboard else 0
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/diagnose",
            json=data
        )

        st.write("API Status Code:", response.status_code)

        if response.status_code == 200:

            result = response.json()

            st.success("Diagnosis Complete")

            st.subheader("🔍 API Response")
            st.json(result)

        else:
            st.error("API से response नहीं मिला।")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error(
            "FastAPI server चालू नहीं है। "
            "पहले app.py का Uvicorn server start करें।"
        )