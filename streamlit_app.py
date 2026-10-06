import streamlit as st
import os

# Page ki setting
st.set_page_config(
    page_title="CCTNS Dumka IT Helpdesk",
    page_icon="🖥️",
    layout="centered"
)

# --- MODERN CUSTOM CSS FOR PROFESSIONAL UI ---
st.markdown("""
<style>
/* App Background & Font */
.stApp {
    background: linear-gradient(180deg, #F0F3F8 0%, #E2E8F0 100%) !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Saare text ko readable aur dark rakhna */
.stApp, h1, h2, h3, h4, p, label {
    color: #1E293B !important;
}

/* Header Styling */
h1, h2, h3 {
    letter-spacing: -0.5px;
}

/* Checkbox container styling */
div[data-testid="stCheckbox"] {
    background-color: #FFFFFF;
    padding: 8px 12px;
    border-radius: 8px;
    border: 1px solid #E2E8F0;
    margin-bottom: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    transition: all 0.2s ease;
}
div[data-testid="stCheckbox"]:hover {
    border-color: #3B82F6;
    box-shadow: 0 4px 6px rgba(59, 130, 246, 0.1);
}
div[data-testid="stCheckbox"] label p {
    font-size: 16px !important;
    font-weight: 600 !important;
    color: #334155 !important;
}

/* Custom Button Styling */
.stButton>button {
    background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
    color: white !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    padding: 0.75rem 1.5rem !important;
    border-radius: 10px !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
    transition: all 0.3s ease !important;
}
.stButton>button:hover {
    background: linear-gradient(135deg, #1D4ED8 100%, #1E40AF 0%) !important;
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.4) !important;
    transform: translateY(-1px);
}
</style>
""", unsafe_allow_html=True)
# -----------------------------------

# --- TOP BANNER / LOGO LOGIC ---
if os.path.exists("logo.jpeg"):
    st.image("logo.jpeg", width="stretch")
elif os.path.exists("logo.jpg"):
    st.image("logo.jpg", width="stretch")
elif os.path.exists("logo.png"):
    st.image("logo.png", width="stretch")
else:
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%); border-radius: 14px; color: white; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <h1 style="margin: 0; font-size: 28px; color: white !important;">🖥️ CCTNS Dumka IT Helpdesk</h1>
        <p style="margin: 5px 0 0 0; font-size: 15px; color: #E2E8F0 !important;">Technical Support & Troubleshooting Portal</p>
    </div>
    """, unsafe_allow_html=True)
# --------------------------
    
# =========================================================
# KNOWLEDGE BASE (Enhanced Cards for All Solutions)
# =========================================================
KNOWLEDGE_BASE = {
    "power": {
        "problem": "CPU/Computer ON nahi ho raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #e74c3c; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #c0392b; margin-top: 0; margin-bottom: 12px; font-size: 18px; display: flex; align-items: center; gap: 8px;">🔌 1. पावर सॉकेट, यूपीएस और पावर केबल की जाँच</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5; margin-bottom: 10px;">सुनिश्चित करें कि मुख्य पावर सॉकेट और यूपीएस (UPS) चालू हैं। दीवार के सॉकेट से यूपीएस और सीपीयू तक आने वाली पावर केबल दोनों सिरों पर कसकर जुड़ी होनी चाहिए।</p>
    <div style="background: #f8f9fa; padding: 10px 14px; border-radius: 6px; border: 1px solid #dee2e6; font-size: 14px; color: #495057;"><b>🔍 कैसे जाँचें:</b> सॉकेट में कोई अन्य उपकरण (जैसे मोबाइल चार्जर) लगाकर देखें कि बिजली आ रही है या नहीं। यूपीएस की इंडिकेटर लाइट चालू होनी चाहिए।</div>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #e67e22; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #d35400; margin-top: 0; margin-bottom: 12px; font-size: 18px; display: flex; align-items: center; gap: 8px;">⚡ 2. एसएमपीएस (SMPS) का रियर स्विच देखें</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5; margin-bottom: 10px;">सीपीयू कैबिनेट के पिछले हिस्से में लगे पावर सप्लाई यूनिट (SMPS) के मुख्य स्विच को देखें।</p>
    <div style="background: #f8f9fa; padding: 10px 14px; border-radius: 6px; border: 1px solid #dee2e6; font-size: 14px; color: #495057;"><b>🔍 कैसे जाँचें:</b> सुनिश्चित करें कि रियर स्विच <b>'I' (ON)</b> स्थिति में है, न कि 'O' (OFF) स्थिति में।</div>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #f1c40f; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #b7950b; margin-top: 0; margin-bottom: 12px; font-size: 18px; display: flex; align-items: center; gap: 8px;">🔘 3. कैबिनेट पावर बटन की जाँच करें</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5; margin-bottom: 10px;">सीपीयू के सामने वाले पावर बटन को दबाकर देखें। कई बार बटन अंदर की तरफ फंस जाता है या उसका इंटरनल कनेक्टर मदरबोर्ड से ढीला हो जाता है (Front Panel Header)।</p>
    <div style="background: #f8f9fa; padding: 10px 14px; border-radius: 6px; border: 1px solid #dee2e6; font-size: 14px; color: #495057;"><b>🔍 कैसे जाँचें:</b> बटन दबाने पर यदि मदरबोर्ड पर कोई छोटी इंडिकेटर लाइट जलती है या पंखा हल्का सा हिलता है, तो इसका मतलब पावर मिल रही है।</div>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #3498db; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #2980b9; margin-top: 0; margin-bottom: 12px; font-size: 18px; display: flex; align-items: center; gap: 8px;">🔌 4. 24-pin मदरबोर्ड और CPU पावर कनेक्टर जाँचें</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5; margin-bottom: 10px;">कैबिनेट का ढक्कन खोलकर अंदर देखें कि क्या सभी मुख्य पावर केबल्स अपने पोर्ट पर ठीक से लगी हैं या नहीं। इसमें मुख्य <b>24-pin मदरबोर्ड कनेक्टर</b> और <b>4/8-pin CPU पावर कनेक्टर</b> शामिल हैं।</p>
    <div style="background: #f8f9fa; padding: 10px 14px; border-radius: 6px; border: 1px solid #dee2e6; font-size: 14px; color: #495057;"><b>🔍 कैसे जाँचें:</b> दोनों कनेक्टर्स को हल्के से खींचकर चेक करें कि वे अपनी जगह पर मजबूती से लॉक हैं या नहीं।</div>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #27ae60; margin-top: 0; margin-bottom: 12px; font-size: 18px; display: flex; align-items: center; gap: 8px;">🏛️ 5. CCTNS ऑफिस दुमका तकनीकी सहायता</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5; margin-bottom: 10px;">यदि उपरोक्त सभी बुनियादी जाँच के बाद भी समस्या बनी रहती है, तो हार्डवेयर स्तर की गहरी जाँच के लिए CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करके सिस्टम का निरीक्षण करवाएं।</p>
    <div style="background: #f8f9fa; padding: 10px 14px; border-radius: 6px; border: 1px solid #dee2e6; font-size: 14px; color: #495057;"><b>🔍 कैसे जाँचें:</b> तकनीकी टीम मल्टीमीटर या पोस्ट कार्ड (POST card) के माध्यम से वोल्टेज और मदरबोर्ड के फॉल्ट की पुष्टि करेगी।</div>
</div>
        """,
        "confidence": "High"
    },
    "display": {
        "problem": "Monitor par Display nahi aa raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #3498db; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #2980b9; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🖥️ 1. मॉनिटर पावर और डिस्प्ले केबल जाँच</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">HDMI/VGA/DisplayPort केबल को दोनों सिरों (मॉनिटर और सीपीयू) पर दोबारा कसकर कनेक्ट करें। सुनिश्चित करें कि मॉनिटर का पावर एडप्टर चालू है।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #e67e22; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #d35400; margin-top: 0; margin-bottom: 12px; font-size: 18px;">⚙️ 2. इनपुट सोर्स और हार्डवेयर जाँच</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">मॉनिटर के मेनू बटन से सही <b>Input Source</b> (जैसे HDMI 1 या VGA) सेलेक्ट करें। रैम (RAM) को निकालकर साफ करके दोबारा लगाएं या दूसरे मॉनिटर से टेस्ट करें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #27ae60; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🏛️ 3. CCTNS ऑफिस दुमका तकनीकी सहायता</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">समस्या ठीक न होने पर CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क कर सहायता लें।</p>
</div>
        """,
        "confidence": "High"
    },
    "os": {
        "problem": "Windows/OS Load nahi ho raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #8e44ad; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #8e44ad; margin-top: 0; margin-bottom: 12px; font-size: 18px;">💽 1. एक्सटर्नल डिवाइसेस और स्टोरेज जाँच</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">सभी अनावश्यक USB पेनड्राइव या एक्सटर्नल हार्ड डिस्क हटा दें। BIOS/UEFI में जाकर चेक करें कि SSD/HDD डिटेक्ट हो रहा है या नहीं और Boot Order सही है या नहीं।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #2980b9; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #2980b9; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🛠️ 2. स्टार्टअप रिपेयर और रीइंस्टॉल</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">Windows Recovery Environment में जाकर <b>Startup Repair</b> ट्राय करें। जरूरत पड़ने पर डेटा बैकअप लेकर OS रीइंस्टॉल करें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #27ae60; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🏛️ 3. CCTNS ऑफिस दुमका तकनीकी सहायता</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">विशेषज्ञ मार्गदर्शन के लिए CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "High"
    },
    "beep": {
        "problem": "Motherboard se Beep aa rahi hai",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #d35400; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #d35400; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🔔 1. रैम (RAM) और कंपोनेंट्स की जाँच</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">कंप्यूटर बंद करके पावर केबल निकालें। RAM मॉड्यूल को बाहर निकालकर उसके पिन को साफ करें और सही से दोबारा लगाएं। बीप पैटर्न नोट करके मदरबोर्ड मैन्युअल से मैच करें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #27ae60; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🏛️ 2. CCTNS ऑफिस दुमका तकनीकी सहायता</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">यदि बीप साउंड बंद न हो, तो CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "High"
    },
    "shutdown": {
        "problem": "System achanak band ho jata hai",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #c0392b; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #c0392b; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🌡️ 1. कूलिंग और डस्ट क्लीनिंग</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">CPU/GPU का तापमान और कूलिंग फैन चेक करें (ओवरहीटिंग की वजह से ऐसा हो सकता है)। कैबिनेट की धूल साफ करें और थर्मल पेस्ट की जाँच करें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #27ae60; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🏛️ 2. CCTNS ऑफिस दुमका तकनीकी सहायता</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">हार्डवेयर फॉल्ट होने पर CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "Medium"
    },
    "keyboard": {
        "problem": "Keyboard kaam nahi kar raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #2980b9; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #2980b9; margin-top: 0; margin-bottom: 12px; font-size: 18px;">⌨️ 1. पोर्ट और कनेक्शन जाँच</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">कीबोर्ड की USB केबल को दूसरे USB पोर्ट में लगाकर देखें या किसी दूसरे वर्किंग कीबोर्ड से टेस्ट करें। वायरलेस हो तो बैटरी और रिसीवर चेक करें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #27ae60; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🏛️ 2. CCTNS ऑफिस दुमका तकनीकी सहायता</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">पोर्ट या ड्राइवर की समस्या के लिए CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "Medium"
    },
    "mouse": {
        "problem": "Mouse kaam nahi kar raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #16a085; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #16a085; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🖱️️ 1. सेंसर और USB पोर्ट जाँच</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">माउस के नीचे का ऑप्टिकल सेंसर साफ करें। इसे दूसरे USB पोर्ट में प्लग करके चेक करें या दूसरे माउस से टेस्ट करें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #27ae60; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🏛️️ 2. CCTNS ऑफिस दुमका तकनीकी सहायता</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">अतिरिक्त सहायता के लिए CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "Medium"
    },
    "time": {
        "problem": "Date/Time automatic badal raha hai",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #8e44ad; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #8e44ad; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🕒 1. विंडोज सेटिंग्स और CMOS बैटरी</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">Windows Settings > Time & language में जाकर <b>Set time automatically</b> ऑन करें। यदि पीसी बंद होने पर बार-बार समय रीसेट होता है, तो मदरबोर्ड की <b>CMOS Battery (CR2032)</b> बदलें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #27ae60; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🏛️ 2. CCTNS ऑफिस दुमका तकनीकी सहायता</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">बैटरी बदलने या तकनीकी सहायता के लिए CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "High"
    },
    "usb": {
        "problem": "USB Port kaam nahi kar raha",
        "solution": """
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #2980b9; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #2980b9; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🔌 1. डिवाइस मैनेजर और पोर्ट जाँच</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">डिवाइस को दूसरे पोर्ट में चेक करें। Device Manager > Universal Serial Bus controllers में जाकर ड्राइवर एरर चेक करें और रीस्टार्ट करें।</p>
</div>
<div style="background: #ffffff; padding: 20px; border-radius: 12px; border-left: 6px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
    <h4 style="color: #27ae60; margin-top: 0; margin-bottom: 12px; font-size: 18px;">🏛️ 2. CCTNS ऑफिस दुमका तकनीकी सहायता</h4>
    <p style="color: #2c3e50; font-size: 15px; line-height: 1.5;">फिजिकल डैमेज होने पर CCTNS Office Dumka में <b>Er. Bidhan Chandra Singh</b> से संपर्क करें।</p>
</div>
        """,
        "confidence": "Medium"
    }
}

st.markdown("---")

st.markdown("### 🔍 Troubleshooting Symptoms")
st.write("कृपया सिस्टम में आ रही समस्या (Symptom) को नीचे से चुनें:")

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

if st.button("🔍 Diagnose Problem Now", use_container_width=True):
    
    # --- SMART VALIDATION ---
    if not (power or display or os_loading or keyboard or mouse or beep or time_change or usb or shutdown):
        st.warning("⚠️ कृपया समस्या का निदान करने के लिए कम से कम एक विकल्प (Symptom) चुनें!")
    else:
        # --- LOCAL DIAGNOSIS LOGIC ---
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
            extra_html = f'<div style="background: #FFFBEB; padding: 15px; border-radius: 8px; border: 1px solid #FDE68A; margin-top: 15px;"><h4 style="color: #B45309; margin: 0 0 8px 0; font-size: 16px;">📌 अन्य चुनी गई समस्याओं के त्वरित उपाय:</h4><ul style="color: #78350F; font-size: 15px; margin: 0; padding-left: 20px; line-height: 1.5;">{extra_solutions}</ul></div>'
        
        html_ui = f"""
        <div style="background-color: #FFFFFF; padding: 25px; border-radius: 14px; border: 1px solid #CBD5E1; box-shadow: 0 10px 25px rgba(0,0,0,0.06); margin-top: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #F1F5F9; padding-bottom: 12px; margin-bottom: 20px;">
                <h3 style="color: #2563EB; margin: 0; font-size: 20px;">🛠️ Main Solution (मुख्य उपाय)</h3>
                <span style="background: #EFF6FF; color: #1D4ED8; padding: 4px 10px; border-radius: 6px; font-size: 13px; font-weight: 600;">Confidence: {confidence}</span>
            </div>
            
            {primary_solution}
            
            {extra_html}
            
            <div style="background-color: #F8FAFC; padding: 14px 18px; border-radius: 8px; border: 1px solid #E2E8F0; margin-top: 20px; display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #64748B; font-size: 14px;"><b>Primary Root Cause:</b> <span style="color: #EF4444; font-weight: 600;">{primary_problem}</span></span>
            </div>
        </div>
        """
        
        st.markdown(html_ui, unsafe_allow_html=True)

# --- FOOTER AUR DISCLAIMER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #64748B; padding: 20px; border-top: 1px solid #CBD5E1; margin-top: 30px;">
    <h4 style="margin: 0; color: #2563EB; font-size: 16px; letter-spacing: 0.5px;">For IT Helpdesk Support - Dumka District</h4>
    <p style="margin-top: 4px; font-size: 12px; font-style: italic;">⚠️ Disclaimer: Ye AI Assistant hai, official CCTNS data se directly connected nahi.</p>
</div>
""", unsafe_allow_html=True)