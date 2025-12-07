## Automation-Using-Python

Welcome to **Automation Using Python**, a collection of automation-focused Python tools designed to simplify repetitive tasks, boost productivity, and demonstrate the power of Python-based automation.  
Each project is self-contained with its own main code file and README for instructions.

---

## 📂 Project Structure

```

Automation-Using-Python/                
│
├── WhatsApp-Auto-Messenger/            # Automates sending WhatsApp messages
│   ├── whatsapp_messenger.py           # Main script for WhatsApp automation
│   └── README.md                       # Documentation for WhatsApp Messenger
│
├── Phone-Tracer/                       # Tracks phone details via number lookup
│   ├── phone_tracer.py                 # Main script for phone tracing
│   └── README.md                       # Documentation for Phone Tracer
│
├── Text-To-Speech/                     # Converts text into speech using Python
│   ├── text_to_speech.py               # Main script for TTS conversion
│   └── README.md                       # Documentation for Text-To-Speech
│
├── Website-Launcher/                   # Opens websites automatically
│   ├── website_launcher.py             # Main application script
│   └── README.md                       # Project documentation
│
├── Notepad/                            # Simple Notepad application using Python
│   ├── notepad_app.py                  # Main Notepad GUI application
│   └── README.md                       # Documentation for Notepad
│
└── README.md                           # Root documentation for all projects

```

---

## 🚀 Included Projects

### 1. WhatsApp Auto Messenger 💬  
A simple GUI tool to **instantly send WhatsApp messages** using Python.  
Enter the phone number + message → sends automatically through WhatsApp Web.

**✨ Features:**  
- Send messages instantly  
- Clean Tkinter GUI  
- Supports any phone number  
- Uses `pywhatkit` for automation  

**File:** `whatsapp_messenger.py`

---

### 2. Phone Tracer 🔍  
A Python-based tool to **trace basic information about a phone number**, such as:  
- Country  
- Carrier  
- Region  
- Time zone  

Uses open-source Python libraries for analyzing phone number metadata.

**File:** `phone_tracer.py`

---

### 3. Text-To-Speech 🎤

A clean Tkinter-based GUI application that converts **typed text into speech** using the offline engine `pyttsx3`.

**✨ Features:**
- Convert any text to speech  
- Offline (no internet needed)  
- Smooth and simple GUI  
- Adjustable speaking rate  

**File:** `text_to_speech.py`

---

### 4. Website Launcher 🌐

A Python GUI app to **open any website instantly** from a list or custom URL.
Useful for quick website launching and productivity.

**✨ Features**

- One-click website launching
- Add your own website URLs
- Fast & lightweight GUI
- Uses Python’s built-in `webbrowser` module
  
**File**: `website_launcher.py`

---
### 5. Notepad 📝

A **modern and enhanced Notepad application** built using Python & Tkinter.

**✨ Features**

- 🔢 Line numbers
- 🧮 Live word count
- 🔍 Search & Replace (Ctrl + F)
- 💾 Auto-save every 10 seconds
- 🌙 Dark Mode
- 🔠 Font resizing
- 📁 New / Open / Save / Save As
- ↩️ Undo / Redo
- ⌨️ Keyboard shortcuts

**File:** `notepad_app.py`

---

## Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/ShakalBhau0001/Automation-Using-Python.git
```

2. **Navigate to a project folder**
```bash
cd Automation-Using-Python/WhatsApp-Auto-Messenger
```

3. **Install dependencies (if required)**
```bash
pip install -r requirements.txt
```

4. **Run the project**
```bash
python whatsapp_messenger.py
```

---

## 🧰 Technologies Used

- **Python 3.8+**
- **Tkinter** → GUI
- **PyWhatKit** → WhatsApp Automation
- **phonenumbers** → For Phone Tracing
- **pyttsx3** → Offline Text-To-Speech
- **webbrowser** → Website Launcher

---

## 💡 Author

Made with ❤️ by **_ShakalBhau0001_**

---
