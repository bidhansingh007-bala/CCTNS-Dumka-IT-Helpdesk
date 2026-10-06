import streamlit as st
import os

# Page ki setting
st.set_page_config(
    page_title="CCTNS Dumka - IT Helpdesk Portal",
    page_icon="🖥️",
    layout="wide"
)

# --- eSUMMON PORTAL INSPIRED CUSTOM CSS ---
st.markdown("""
<style>
/* App Background */
.stApp {
    background-color: #F1F5F9 !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Top Dark Blue Header Banner */
.portal-header {
    background: linear-gradient(90deg, #0A192F 0%, #1E3A8A 50%, #0A192F 100%);
    padding: 15px 25px;
    border-radius: 6px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}
.portal-title {
    font-size: 24px;
    font-weight: 700;
    color: #FFFFFF !important;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 12px;
}

/* Navigation Bar */
.nav-bar {
    background-color: #FFFFFF;
    padding: 10px 20px;
    border-radius: 6px;
    border: 1px solid #E2E8F0;
    display: flex;
    gap: 20px;
    font-size: 14px;
    font-weight: 600;
    color: #475569;
    margin-bottom: 15px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}
.nav-item {
    cursor: pointer;
    padding: 5px 10px;
    border-radius: 4px;
    transition: all 0.2s;
}
.nav-item.active {
    background-color: #1E3A8A;
    color: white !important;
}

/* Alert Banner */
.alert-banner {
    background-color: #FEF2F2;
    border: 1px solid #FCA5A5;
    color: #991B1B;
    padding: 10px 15px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 500;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* Checkbox container styling */
div[data-testid="stCheckbox"] {
    background-color: #FFFFFF;
    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid #E2E8F0;
    margin-bottom: 10px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}
div[data-testid="stCheckbox"] label p {
    font-size: 15px !important;
    font-weight: 600 !important;
    color: #1E293B !important;
}

/* Custom Button Styling */
.stButton>button {
    background: linear-gradient(135deg, #F97316 0%, #EA580C 100%) !important;
    color: white !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    padding: 0.6rem 1.2rem !important;
    border-radius: 8px !important;
    border: none !important;
    box-shadow: 0 4px 10px rgba(249, 115, 22, 0.3) !important;
    width: 100%;
}
.stButton>button:hover {
    background: linear-gradient(135deg, #EA580C 0%, #C2410C 100%) !important;
}
</style>
""", unsafe_allow_html=True)

# --- PORTAL HEADER (eSummon Style) ---
st.markdown("""
<div class="portal-header">
    <div class="portal-title">
        <span>🖥️</span> CCTNS Dumka - IT Helpdesk & Support Portal
    </div>
    <div style="font-size: 13px; color: #93C5FD; font-weight: 500;">
        Office of the Superintendent of Police | Dumka, Jharkhand
    </div>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION BAR ---
st.markdown("""
<div class="nav-bar">
    <span class="nav-item active">🏠 Home</span>
    <span class="nav-item">📊 System Monitoring</span>
    <span class="nav-item">📜 Hardware History</span>
    <span class="nav-item">🔍 Quick Diagnosis</span>
    <span class="nav-item">📋 Reports</span>
</div>
""", unsafe_allow_html=True)

# --- ALERT NOTICE BANNER ---
st.markdown("""
<div class="alert-banner">
    <span>⚠️</span> <b>Notice:</b> Unresolved hardware issues persisting for more than 48 hours must be escalated directly to the district technical cell.
</div>
""", unsafe_allow_html=True)

# =========================================================
# KNOWLEDGE BASE
# =========================================================
KNOWLEDGE_BASE = {
    "power": {
        "problem": "CPU/Computer ON nahi ho raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #EF4444; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #DC2626; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🔌 1. पावर सॉकेट, यूपीएस और पावर केबल की जाँच</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5; margin-bottom: 8px;">सुनिश्चित करें कि मुख्य पावर सॉकेट और यूपीएस (UPS) चालू हैं। दीवार के सॉकेट से यूपीएस और सीपीयू तक आने वाली पावर केबल कसकर जुड़ी हो।</p>
    <div style="background: #F8FAFC; padding: 8px 12px; border-radius: 6px; border: 1px solid #E2E8F0; font-size: 13px; color: #475569;"><b>🔍 कैसे जाँचें:</b> सॉकेट में दूसरा उपकरण (जैसे चार्जर) लगाकर चेक करें। यूपीएस की इंडिकेटर लाइट चालू होनी चाहिए।</div>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #F59E0B; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #D97706; margin-top: 0; margin-bottom: 8px; font-size: 17px;">⚡ 2. एसएमपीएस (SMPS) का रियर स्विच देखें</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5; margin-bottom: 8px;">सीपीयू कैबिनेट के पिछले हिस्से में लगे पावर सप्लाई यूनिट (SMPS) के मुख्य स्विच को देखें।</p>
    <div style="background: #F8FAFC; padding: 8px 12px; border-radius: 6px; border: 1px solid #E2E8F0; font-size: 13px; color: #475569;"><b>🔍 कैसे जाँचें:</b> सुनिश्चित करें कि रियर स्विच <b>'I' (ON)</b> स्थिति में है, न कि 'O' (OFF) स्थिति में।</div>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #3B82F6; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #2563EB; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🔌 3. 24-pin मदरबोर्ड और CPU पावर कनेक्टर जाँचें</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5; margin-bottom: 8px;">कैबिनेट खोलकर अंदर मुख्य <b>24-pin मदरबोर्ड कनेक्टर</b> और <b>4/8-pin CPU पावर कनेक्टर</b> की फिटिंग चेक करें।</p>
    <div style="background: #F8FAFC; padding: 8px 12px; border-radius: 6px; border: 1px solid #E2E8F0; font-size: 13px; color: #475569;"><b>🔍 कैसे जाँचें:</b> दोनों कनेक्टर्स को हल्के से खींचकर देखें कि वे मजबूती से लॉक हैं या नहीं।</div>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #10B981; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #059669; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🏛️ 4. CCTNS ऑफिस दुमका तकनीकी सहायता</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5; margin-bottom: 8px;">समस्या हल न होने पर CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करके निरीक्षण करवाएं।</p>
</div>
        """,
        "confidence": "High"
    },
    "display": {
        "problem": "Monitor par Display nahi aa raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #3B82F6; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #2563EB; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🖥️ 1. मॉनिटर पावर और डिस्प्ले केबल जाँच</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">HDMI/VGA केबल को दोनों सिरों पर कसकर कनेक्ट करें और इनपुट सोर्स सही चुनें। रैम (RAM) को निकालकर साफ करके दोबारा लगाएं।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #10B981; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #059669; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🏛️ 2. तकनीकी सहायता</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "High"
    },
    "os": {
        "problem": "Windows/OS Load nahi ho raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #8B5CF6; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #7C3AED; margin-top: 0; margin-bottom: 8px; font-size: 17px;">💽 1. स्टोरेज और स्टार्टअप जाँच</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">अनावश्यक USB डिवाइस हटाकर BIOS में SSD/HDD डिटेक्शन चेक करें। Startup Repair ट्राय करें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #10B981; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #059669; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🏛️ 2. तकनीकी सहायता</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "High"
    },
    "beep": {
        "problem": "Motherboard se Beep aa rahi hai",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #F59E0B; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #D97706; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🔔 1. रैम (RAM) क्लीनिंग</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">रैम निकालकर उसके पिन को साफ करें और सही से लगाएं। बीप पैटर्न नोट करें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #10B981; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #059669; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🏛️ 2. तकनीकी सहायता</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "High"
    },
    "shutdown": {
        "problem": "System achanak band ho jata hai",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #EF4444; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #DC2626; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🌡 1. कूलिंग और डस्ट क्लीनिंग</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">CPU फैन और कूलिंग चेक करें (Overheating से बचाव)। कैबिनेट की धूल साफ करें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #10B981; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #059669; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🏛️ 2. तकनीकी सहायता</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "Medium"
    },
    "keyboard": {
        "problem": "Keyboard kaam nahi kar raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #3B82F6; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #2563EB; margin-top: 0; margin-bottom: 8px; font-size: 17px;">⌨️ 1. पोर्ट और कनेक्शन जाँच</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">कीबोर्ड को दूसरे USB पोर्ट में लगाएं या दूसरे कीबोर्ड से टेस्ट करें।</p>
</div>
        """,
        "confidence": "Medium"
    },
    "mouse": {
        "problem": "Mouse kaam nahi kar raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #10B981; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #059669; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🖱️ 1. सेंसर और USB पोर्ट जाँच</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">माउस का ऑप्टिकल सेंसर साफ करें और दूसरे पोर्ट में चेक करें।</p>
</div>
        """,
        "confidence": "Medium"
    },
    "time": {
        "problem": "Date/Time automatic badal raha hai",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #8B5CF6; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #7C3AED; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🕒 1. CMOS बैटरी रिप्लेसमेंट</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">Windows सेटिंग्स में ऑटो टाइम ऑन करें। समय रीसेट होने पर <b>CMOS Battery (CR2032)</b> बदलें।</p>
</div>
        """,
        "confidence": "High"
    },
    "usb": {
        "problem": "USB Port kaam nahi kar raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #3B82F6; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 12px;">
    <h4 style="color: #2563EB; margin-top: 0; margin-bottom: 8px; font-size: 17px;">🔌 1. ड्राइवर और पोर्ट जाँच</h4>
    <p style="color: #334155; font-size: 14px; line-height: 1.5;">Device Manager में जाकर USB कंट्रोलर ड्राइवर एरर चेक करें और रीस्टार्ट करें।</p>
</div>
        """,
        "confidence": "Medium"
    }
}

st.markdown("### 🔍 Select System Symptoms (समस्या चुनें)")

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

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Run System Diagnosis", use_container_width=True):
    
    if not (power or display or os_loading or keyboard or mouse or beep or time_change or usb or shutdown):
        st.warning("⚠️ कृपया निदान के लिए कम से कम एक लक्षण (Symptom) चुनें!")
    else:
        result = {}
        if power: result = KNOWLEDGE_BASE["power"]
        elif display: result = KNOWLEDGE_BASE["display"]
        elif os_loading: result = KNOWLEDGE_BASE["os"]
        elif beep: result = KNOWLEDGE_BASE["beep"]
        elif shutdown: result = KNOWLEDGE_BASE["shutdown"]
        elif keyboard: result = KNOWLEDGE_BASE["keyboard"]
        elif mouse: result = KNOWLEDGE_BASE["mouse"]
        elif time_change: result = KNOWLEDGE_BASE["time"]
        elif usb: result = KNOWLEDGE_BASE["usb"]

        primary_solution = result['solution']
        confidence = result['confidence']
        
        extra_solutions = ""
        if keyboard and "Keyboard" not in result['problem']:
            extra_solutions += "<li style='margin-bottom: 6px;'><b>Keyboard:</b> USB cable बदलकर दूसरे Port में लगायें।</li>"
        if mouse and "Mouse" not in result['problem']:
            extra_solutions += "<li style='margin-bottom: 6px;'><b>Mouse:</b> ऑप्टिकल सेंसर साफ करें।</li>"
        if time_change and "Date/Time" not in result['problem']:
            extra_solutions += "<li style='margin-bottom: 6px;'><b>Date/Time:</b> CMOS Battery (CR2032) चेक करें।</li>"
        if usb and "USB Port" not in result['problem']:
            extra_solutions += "<li style='margin-bottom: 6px;'><b>USB Port:</b> ड्राइवर अपडेट करें।</li>"
        if shutdown and "System" not in result['problem']:
            extra_solutions += "<li style='margin-bottom: 6px;'><b>Auto Shutdown:</b> CPU Fan और Thermal Paste चेक करें।</li>"
        if beep and "Beep" not in result['problem']:
            extra_solutions += "<li style='margin-bottom: 6px;'><b>Beep Sound:</b> RAM निकालकर साफ करें।</li>"
        
        extra_html = ""
        if extra_solutions != "":
            extra_html = f'<div style="background: #FFFBEB; padding: 12px; border-radius: 6px; border: 1px solid #FDE68A; margin-top: 12px;"><h4 style="color: #B45309; margin: 0 0 6px 0; font-size: 14px;">📌 अन्य चुनी गई समस्याओं के उपाय:</h4><ul style="color: #78350F; font-size: 13px; margin: 0; padding-left: 18px;">{extra_solutions}</ul></div>'
        
        portal_result_ui = f"""
        <div style="background-color: #FFFFFF; padding: 25px; border-radius: 10px; border: 1px solid #CBD5E1; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-top: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #F1F5F9; padding-bottom: 10px; margin-bottom: 15px;">
                <h3 style="color: #1E3A8A; margin: 0; font-size: 18px;">🛠️ Diagnostic Report & Solutions</h3>
                <span style="background: #EFF6FF; color: #1D4ED8; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: 600;">Confidence: {confidence}</span>
            </div>
            
            {primary_solution}
            
            {extra_html}
        </div>
        """
        st.markdown(portal_result_ui, unsafe_allow_html=True)

