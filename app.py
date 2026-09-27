
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="CCTNS Dumka IT Helpdesk",
    description="Computer Hardware & Windows Troubleshooting API",
    version="1.0"
)


# =========================================================
# REQUEST MODEL
# =========================================================

class DiagnosisRequest(BaseModel):

    power_on: int = 1
    display_on: int = 1
    os_loading: int = 1
    key_board: int = 1
    mouse: int = 1
    beep_sound: int = 0
    time_automatic_change: int = 0
    USB_port_not_working: int = 0
    automatic_shut_down: int = 0
    motherboard_problem: int = 0


# =========================================================
# KNOWLEDGE BASE
# =========================================================

KNOWLEDGE_BASE = {

    "power": {
        "problem": "CPU/Computer ON nahi ho raha",
        "solution": (
            "Power socket, UPS aur power cable check karein. "
            "SMPS ka rear switch ON hai ya nahi dekhein. "
            "24-pin motherboard aur CPU power connector check karein. "
            "Power button ki jaanch karein. "
            "Zarurat ho to CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein."
        ),
        "confidence": "High"
    },

    "display": {
        "problem": "Monitor par Display nahi aa raha",
        "solution": (
            "Monitor power aur display cable check karein. "
            "HDMI/VGA/DisplayPort cable ko dobara connect karein. "
            "Monitor ka correct Input Source select karein. "
            "RAM ko safely reseat karke test karein. "
            "Dedicated GPU ho to uski seating aur power check karein. "
            "Possible ho to doosre monitor se test karein. "
	    "CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein. "
        ),
        "confidence": "High"
    },

    "os": {
        "problem": "Windows/OS Load nahi ho raha",
        "solution": (
            "Unnecessary USB devices remove karein. "
            "BIOS/UEFI mein SSD/HDD detect ho raha hai ya nahi check karein. "
            "Boot Order check karein. "
            "Windows Recovery Environment mein Startup Repair try karein. "
            "Zaruri data ka backup lekar hi reinstall/format karein."
	    "CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein. "
        ),
        "confidence": "High"
    },

    "keyboard": {
        "problem": "Keyboard kaam nahi kar raha",
        "solution": (
            "Keyboard ko doosre USB port mein lagakar dekhein. "
            "Doosre keyboard se test karein. "
            "Wireless keyboard ho to battery aur receiver check karein. "
            "Device Manager mein keyboard device check karein."
	    "CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein. "
        ),
        "confidence": "Medium"
    },

    "mouse": {
        "problem": "Mouse kaam nahi kar raha",
        "solution": (
            "Mouse ko doosre USB port mein lagakar dekhein. "
            "Doosre mouse se test karein. "
            "Wireless mouse ki battery aur receiver check karein. "
            "Optical sensor clean karein aur Device Manager check karein."
	    "CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein. "
        ),
        "confidence": "Medium"
    },

    "beep": {
        "problem": "Motherboard se Beep aa rahi hai",
        "solution": (
            "Computer band karke power cable remove karein. "
            "RAM ko safely reseat karein aur zarurat par ek-ek RAM module "
            "se test karein. Dedicated GPU ki seating check karein. "
            "Beep pattern note karke motherboard/BIOS manual ke beep code "
            "se compare karein."
	    "CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein. "
        ),
        "confidence": "High"
    },

    "time": {
        "problem": "Date/Time automatic badal raha hai",
        "solution": (
            "Windows Settings > Time & language > Date & time mein "
            "Set time automatically ON karein aur correct Time Zone select karein. "
            "Agar PC band hone ke baad time reset hota hai to CMOS/RTC "
            "battery, aam taur par CR2032, check/replace karein."
	    "CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein. "
        ),
        "confidence": "High"
    },

    "usb": {
        "problem": "USB Port kaam nahi kar raha",
        "solution": (
            "Device ko doosre USB port mein lagakar test karein. "
            "Same port mein doosra known-good device test karein. "
            "Computer restart karein. "
            "Device Manager > Universal Serial Bus controllers mein "
            "warning/error check karein. Physical damage ho to technician ko dikhayein."
	    "CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein. "
        ),
        "confidence": "Medium"
    },

    "shutdown": {
        "problem": "System achanak band ho jata hai",
        "solution": (
            "CPU/GPU temperature aur cooling fans check karein. "
            "Cabinet ki dust clean karein. "
            "UPS/SMPS aur power cable check karein. "
            "RAM reseat karke test karein. "
            "Windows Event Viewer mein unexpected shutdown errors check karein."
	    "CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein. "
        ),
        "confidence": "Medium"
    },

    "motherboard": {
        "problem": "Motherboard mein hardware problem ki sambhawana",
        "solution": (
            "Sirf No Display ke basis par motherboard ko faulty declare na karein. "
            "Pehle PSU, RAM, GPU, power connectors aur POST/BIOS symptoms check karein. "
            "Burning smell, physical damage ya repeated hardware failure ho to "
            "qualified technician se motherboard diagnosis karayein."
	    "CCTNS Office Dumka Er. Bidhan Chandra Singh se baat kar ke test karein. "
        ),
        "confidence": "Medium"
    }
}


# =========================================================
# ROOT API
# =========================================================

@app.get("/")
def home():

    return {
        "Application": "CCTNS Dumka IT Helpdesk",
        "Status": "Running",
        "Version": "1.0"
    }


# =========================================================
# DIAGNOSE API
# =========================================================

@app.post("/diagnose")
def diagnose(data: DiagnosisRequest):

    # -----------------------------------------------------
    # 1. POWER HAS HIGHEST PRIORITY
    # -----------------------------------------------------

    if data.power_on == 0:

        result = KNOWLEDGE_BASE["power"]

        return {
            "Problem_Kha_Hai": result["problem"],
            "Solution_Advice": result["solution"],
            "AI_Ki_Guarantee_Sambhawana": result["confidence"],
            "Priority": "1 - Critical"
        }


    # -----------------------------------------------------
    # 2. NO DISPLAY
    # -----------------------------------------------------

    if data.display_on == 0:

        result = KNOWLEDGE_BASE["display"]

        return {
            "Problem_Kha_Hai": result["problem"],
            "Solution_Advice": result["solution"],
            "AI_Ki_Guarantee_Sambhawana": result["confidence"],
            "Priority": "2 - High"
        }


    # -----------------------------------------------------
    # 3. WINDOWS / OS
    # -----------------------------------------------------

    if data.os_loading == 0:

        result = KNOWLEDGE_BASE["os"]

        return {
            "Problem_Kha_Hai": result["problem"],
            "Solution_Advice": result["solution"],
            "AI_Ki_Guarantee_Sambhawana": result["confidence"],
            "Priority": "3 - High"
        }


    # -----------------------------------------------------
    # 4. BEEP
    # -----------------------------------------------------

    if data.beep_sound == 1:

        result = KNOWLEDGE_BASE["beep"]

        return {
            "Problem_Kha_Hai": result["problem"],
            "Solution_Advice": result["solution"],
            "AI_Ki_Guarantee_Sambhawana": result["confidence"],
            "Priority": "4 - High"
        }


    # -----------------------------------------------------
    # 5. SUDDEN SHUTDOWN
    # -----------------------------------------------------

    if data.automatic_shut_down == 1:

        result = KNOWLEDGE_BASE["shutdown"]

        return {
            "Problem_Kha_Hai": result["problem"],
            "Solution_Advice": result["solution"],
            "AI_Ki_Guarantee_Sambhawana": result["confidence"],
            "Priority": "5 - High"
        }


    # -----------------------------------------------------
    # 6. MOTHERBOARD
    # -----------------------------------------------------

    if data.motherboard_problem == 1:

        result = KNOWLEDGE_BASE["motherboard"]

        return {
            "Problem_Kha_Hai": result["problem"],
            "Solution_Advice": result["solution"],
            "AI_Ki_Guarantee_Sambhawana": result["confidence"],
            "Priority": "6 - Medium"
        }


    # -----------------------------------------------------
    # 7. KEYBOARD
    # -----------------------------------------------------

    if data.key_board == 0:

        result = KNOWLEDGE_BASE["keyboard"]

        return {
            "Problem_Kha_Hai": result["problem"],
            "Solution_Advice": result["solution"],
            "AI_Ki_Guarantee_Sambhawana": result["confidence"],
            "Priority": "7 - Medium"
        }


    # -----------------------------------------------------
    # 8. MOUSE
    # -----------------------------------------------------

    if data.mouse == 0:

        result = KNOWLEDGE_BASE["mouse"]

        return {
            "Problem_Kha_Hai": result["problem"],
            "Solution_Advice": result["solution"],
            "AI_Ki_Guarantee_Sambhawana": result["confidence"],
            "Priority": "8 - Medium"
        }


    # -----------------------------------------------------
    # 9. DATE / TIME
    # -----------------------------------------------------

    if data.time_automatic_change == 1:

        result = KNOWLEDGE_BASE["time"]

        return {
            "Problem_Kha_Hai": result["problem"],
            "Solution_Advice": result["solution"],
            "AI_Ki_Guarantee_Sambhawana": result["confidence"],
            "Priority": "9 - Low"
        }


    # -----------------------------------------------------
    # 10. USB
    # -----------------------------------------------------

    if data.USB_port_not_working == 1:

        result = KNOWLEDGE_BASE["usb"]

        return {
            "Problem_Kha_Hai": result["problem"],
            "Solution_Advice": result["solution"],
            "AI_Ki_Guarantee_Sambhawana": result["confidence"],
            "Priority": "10 - Low"
        }


    # -----------------------------------------------------
    # NO PROBLEM SELECTED
    # -----------------------------------------------------

    return {
        "Problem_Kha_Hai": "Koi specific problem select nahi ki gayi.",
        "Solution_Advice": (
            "Kripya symptoms mein kam se kam ek problem select karein."
        ),
        "AI_Ki_Guarantee_Sambhawana": "N/A",
        "Priority": "None"
    }
