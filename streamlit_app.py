import streamlit as st
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

# --- LOGO DISPLAY LOGIC (Updated Warning Fix) ---
if os.path.exists("logo.jpeg"):
    st.image("logo.jpeg", width="stretch")
elif os.path.exists("logo.jpg"):
    st.image("logo.jpg", width="stretch")
elif os.path.exists("logo.png"):
    st.image("logo.png", width="stretch")
else:
    st.warning("⚠️ Logo nahi dikh raha kyunki GitHub par file ka naam 'logo.jpg' ya 'logo.jpeg' nahi hai.")
    st.title("🖥️ CCTNS Dumka IT Helpdesk")
# --------------------------
    
# =========================================================
# KNOWLEDGE BASE (Backend logic merged here)
# =========================================================
KNOWLEDGE_BASE = {
    "power": {
        "problem": "CPU/Computer ON nahi ho raha",
        "solution": """
<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 20px; border-radius: 12px; border-left: 6px solid #e74c3c; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #c0392b; margin-top: 0; margin-bottom: 12px; font-size: 20px; display: flex; align-items: center; gap: 8px;">
        🔌 1. पावर सॉकेट, यूपीएस और पावर केबल की जाँच
    </h4>
    <p style="color: #2c3e50; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">
        सुनिश्चित करें कि मुख्य पावर सॉकेट और यूपीएस (UPS) चालू हैं। दीवार के सॉकेट से यूपीएस और सीपीयू तक आने वाली पावर केबल दोनों सिरों पर कसकर जुड़ी होनी चाहिए।
    </p>
    <div style="background: #ffffff; padding: 10px 14px; border-radius: 6px; border: 1px solid #dee2e6; font-size: 15px; color: #495057;">
        <b>🔍 कैसे जाँचें:</b> सॉकेट में कोई अन्य उपकरण (जैसे मोबाइल चार्जर) लगाकर देखें कि बिजली आ रही है या नहीं। यूपीएस की इंडिकेटर लाइट चालू होनी चाहिए।
    </div>
</div>

<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 20px; border-radius: 12px; border-left: 6px solid #e67e22; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #d35400; margin-top: 0; margin-bottom: 12px; font-size: 20px; display: flex; align-items: center; gap: 8px;">
        ⚡ 2. एसएमपीएस (SMPS) का रियर स्विच देखें
    </h4>
    <p style="color: #2c3e50; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">
        सीपीयू कैबिनेट के पिछले हिस्से में लगे पावर सप्लाई यूनिट (SMPS) के मुख्य स्विच को देखें।
    </p>
    <div style="background: #ffffff; padding: 10px 14px; border-radius: 6px; border: 1px solid #dee2e6; font-size: 15px; color: #495057;">
        <b>🔍 कैसे जाँचें:</b> सुनिश्चित करें कि रियर स्विच <b>'I' (ON)</b> स्थिति में है, न कि 'O' (OFF) स्थिति में।
    </div>
</div>

<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 20px; border-radius: 12px; border-left: 6px solid #f1c40f; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #b7950b; margin-top: 0; margin-bottom: 12px; font-size: 20px; display: flex; align-items: center; gap: 8px;">
        🔘 3. कैबिनेट पावर बटन की जाँच करें
    </h4>
    <p style="color: #2c3e50; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">
        सीपीयू के सामने वाले पावर बटन को दबाकर देखें। कई बार बटन अंदर की तरफ फंस जाता है या उसका इंटरनल कनेक्टर मदरबोर्ड से ढीला हो जाता है (Front Panel Header)।
    </p>
    <div style="background: #ffffff; padding: 10px 14px; border-radius: 6px; border: 1px solid #dee2e6; font-size: 15px; color: #495057;">
        <b>🔍 कैसे जाँचें:</b> बटन दबाने पर यदि मदरबोर्ड पर कोई छोटी इंडिकेटर लाइट जलती है या पंखा हल्का सा हिलता है, तो इसका मतलब पावर मिल रही है।
    </div>
</div>

<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 20px; border-radius: 12px; border-left: 6px solid #3498db; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #2980b9; margin-top: 0; margin-bottom: 12px; font-size: 20px; display: flex; align-items: center; gap: 8px;">
        🔌 4. 24-pin मदरबोर्ड और CPU पावर कनेक्टर जाँचें
    </h4>
    <p style="color: #2c3e50; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">
        कैबिनेट का ढक्कन खोलकर अंदर देखें कि क्या सभी मुख्य पावर केबल्स अपने पोर्ट पर ठीक से लगी हैं या नहीं। इसमें मुख्य <b>24-pin मदरबोर्ड कनेक्टर</b> और <b>4/8-pin CPU पावर कनेक्टर</b> शामिल हैं।
    </p>
    <div style="background: #ffffff; padding: 10px 14px; border-radius: 6px; border: 1px solid #dee2e6; font-size: 15px; color: #495057;">
        <b>🔍 कैसे जाँचें:</b> दोनों कनेक्टर्स को हल्के से खींचकर चेक करें कि वे अपनी जगह पर मजबूती से लॉक हैं या नहीं।
    </div>
</div>

<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 20px; border-radius: 12px; border-left: 6px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #27ae60; margin-top: 0; margin-bottom: 12px; font-size: 20px; display: flex; align-items: center; gap: 8px;">
        🏛️ 5. CCTNS ऑफिस दुमका तकनीकी सहायता
    </h4>
    <p style="color: #2c3e50; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">
        यदि उपरोक्त सभी बुनियादी जाँच के बाद भी समस्या बनी रहती है, तो हार्डवेयर स्तर की गहरी जाँच के लिए CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करके सिस्टम का निरीक्षण करवाएं।
    </p>
    <div style="background: #ffffff; padding: 10px 14px; border-radius: 6px; border: 1px solid #dee2e6; font-size: 15px; color: #495057;">
        <b>🔍 कैसे जाँचें:</b> तकनीकी टीम मल्टीमीटर या पोस्ट कार्ड (POST card) के माध्यम से वोल्टेज और मदरबोर्ड के फॉल्ट की पुष्टि करेगी।
    </div>
</div>
        """,
        "confidence": "High"
    },

    },
    "display": {
        "problem": "Monitor par Display nahi aa raha",
        "solution": "Monitor power aur display cable check karein. HDMI/VGA/DisplayPort cable ko dobara connect karein. Monitor ka correct Input Source select karein. RAM ko safely reseat karke test karein. Dedicated GPU ho to uski seating aur power check karein. Possible ho to doosre monitor se test karein. CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein.",
        "confidence": "High"
    },
    "os": {
        "problem": "Windows/OS Load nahi ho raha",
        "solution": "Unnecessary USB devices remove karein. BIOS/UEFI mein SSD/HDD detect ho raha hai ya nahi check karein. Boot Order check karein. Windows Recovery Environment mein Startup Repair try karein. Zaruri data ka backup lekar hi reinstall/format karein. CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein.",
        "confidence": "High"
    },
    "beep": {
        "problem": "Motherboard se Beep aa rahi hai",
        "solution": "Computer band karke power cable remove karein. RAM ko safely reseat karein aur zarurat par ek-ek RAM module se test karein. Dedicated GPU ki seating check karein. Beep pattern note karke motherboard/BIOS manual ke beep code se compare karein. CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein.",
        "confidence": "High"
    },
    "shutdown": {
        "problem": "System achanak band ho jata hai",
        "solution": "CPU/GPU temperature aur cooling fans check karein. Cabinet ki dust clean karein. UPS/SMPS aur power cable check karein. RAM reseat karke test karein. Windows Event Viewer mein unexpected shutdown errors check karein. CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein.",
        "confidence": "Medium"
    },
    "keyboard": {
        "problem": "Keyboard kaam nahi kar raha",
        "solution": "Keyboard ko doosre USB port mein lagakar dekhein. Doosre keyboard se test karein. Wireless keyboard ho to battery aur receiver check karein. Device Manager mein keyboard device check karein. CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein.",
        "confidence": "Medium"
    },
    "mouse": {
        "problem": "Mouse kaam nahi kar raha",
        "solution": "Mouse ko doosre USB port mein lagakar dekhein. Doosre mouse se test karein. Wireless mouse ki battery aur receiver check karein. Optical sensor clean karein aur Device Manager check karein. CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein.",
        "confidence": "Medium"
    },
    "time": {
        "problem": "Date/Time automatic badal raha hai",
        "solution": "Windows Settings > Time & language > Date & time mein Set time automatically ON karein aur correct Time Zone select karein. Agar PC band hone ke baad time reset hota hai to CMOS/RTC battery, aam taur par CR2032, check/replace karein. CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein.",
        "confidence": "High"
    },
    "usb": {
        "problem": "USB Port kaam nahi kar raha",
        "solution": "Device ko doosre USB port mein lagakar test karein. Same port mein doosra known-good device test karein. Computer restart karein. Device Manager > Universal Serial Bus controllers mein warning/error check karein. Physical damage ho to technician ko dikhayein. CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein.",
        "confidence": "Medium"
    }
}

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
        # --- LOCAL DIAGNOSIS LOGIC (No API Call Needed) ---
        result = {}
        
        # Priority Checking
        if power:
            result = KNOWLEDGE_BASE["power"]
        elif display:
            result = KNOWLEDGE_BASE["display"]
        elif os_loading:
            result = KNOWLEDGE_BASE["os"]
        elif beep:
            result = KNOWLEDGE_BASE["beep"]
        elif shutdown:
            result = KNOWLEDGE_BASE["shutdown"]
        elif keyboard:
            result = KNOWLEDGE_BASE["keyboard"]
        elif mouse:
            result = KNOWLEDGE_BASE["mouse"]
        elif time_change:
            result = KNOWLEDGE_BASE["time"]
        elif usb:
            result = KNOWLEDGE_BASE["usb"]

        primary_problem = result['problem']
        primary_solution = result['solution']
        confidence = result['confidence']
        
        extra_solutions = ""
        if keyboard and "Keyboard" not in primary_problem:
            extra_solutions += "<li style='margin-bottom: 8px;'><b>Keyboard:</b> USB cable निकालकर दूसरे Port में लगायें या कीबोर्ड बदलें।</li>"
        if mouse and "Mouse" not in primary_problem:
            extra_solutions += "<li style='margin-bottom: 8px;'><b>Mouse:</b> नीचे का सेंसर साफ करें या दूसरे Port में लगाकर चेक करें।</li>"
        if time_change and "Date/Time" not in primary_problem:
            extra_solutions += "<li style='margin-bottom: 8px;'><b>Date/Time:</b> Motherboard की CMOS Battery (CR2032) खत्म हो गई है, उसे बदलें।</li>"
        if usb and "USB Port" not in primary_problem:
            extra_solutions += "<li style='margin-bottom: 8px;'><b>USB Port:</b> BIOS settings चेक करें या Motherboard का USB Driver अपडेट करें।</li>"
        if shutdown and "System" not in primary_problem:
            extra_solutions += "<li style='margin-bottom: 8px;'><b>Auto Shutdown:</b> CPU Fan चेक करें (Overheating हो सकती है) और Thermal Paste लगायें।</li>"
        if beep and "Beep" not in primary_problem:
            extra_solutions += "<li style='margin-bottom: 8px;'><b>Beep Sound:</b> RAM निकालकर रबर से साफ करें और वापस लगायें।</li>"
        
        extra_html = ""
        if extra_solutions != "":
            extra_html = f'<hr style="border: 1px dashed #AAAAAA; margin: 20px 0;"><h4 style="color: #D35400; margin-bottom: 12px; margin-top: 0px;">📌 अन्य चुनी गई समस्याओं के उपाय:</h4><ul style="color: #333333; font-size: 20px; line-height: 1.4;">{extra_solutions}</ul>'
        
        html_ui = f"""<div style="background-color: #FFFFFF; padding: 25px; border-radius: 12px; border: 2px solid #27AE60; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);">
<h3 style="color: #27AE60; margin-top: 0px; margin-bottom: 10px;">🛠️ Main Solution (मुख्य उपाय):</h3>
<p style="color: #111111; font-size: 26px; font-weight: 900; line-height: 1.4; margin-bottom: 5px;">{primary_solution}</p>
{extra_html}
<hr style="border: 1px solid #DDDDDD; margin: 20px 0;">
<div style="background-color: #F8F9F9; padding: 15px; border-radius: 8px; border: 1px solid #EEEEEE;">
<h4 style="color: #C0392B; margin: 0px 0px 8px 0px;">⚠️ Main Root Cause: <span style="color: #222222; font-weight: bold;">{primary_problem}</span></h4>
<h4 style="color: #2980B9; margin: 0px;">🤖 AI Confidence: <span style="color: #222222; font-weight: bold;">{confidence}</span></h4>
</div>
</div>"""
        
        st.markdown(html_ui, unsafe_allow_html=True)

# --- FOOTER AUR DISCLAIMER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #555555; padding: 15px; border-top: 1px solid #DDDDDD; margin-top: 20px;">
    <h4 style="margin: 0px; color: #27AE60; letter-spacing: 1px;">For IT Helpdesk Support - Dumka District</h4>
    <p style="margin-top: 5px; font-size: 13px; font-style: italic;">⚠️ Disclaimer: Ye AI Assistant hai, official CCTNS data se connected nahi</p>
</div>
""", unsafe_allow_html=True)