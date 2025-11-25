# 📄 WhatsApp Auto Messenger

A simple and clean GUI tool to **instantly send WhatsApp messages** to any phone number using **Python + Tkinter + PyWhatKit**.  
Just enter the **phone number** and **your custom message**, click **Send**, and the app automatically sends it through WhatsApp Web.

---

## ✨ Features

- 🖱️ Easy-to-use graphical interface (Tkinter)  
- 📱 Send messages to **Any WhatsApp Number**  
- ✍️ Fully **enter your message** input  
- ⚡ Instant sending using **pywhatkit.sendwhatmsg_instantly()**  
- 💨 Lightweight — only one external library  
- 🎨 Simple and minimal UI  

---

## 📂 Project Structure

```bash
WhatsApp-Auto-Messenger/
│
├── whatsapp_messenger.py   # Main application
└── README.md               # Project documentation
```

---

## 🧰 Requirements

Make sure you have **Python 3.7+** installed.

**WhatsApp Web must be logged in for this feature to work**

Install the required library:

```bash
pip install pywhatkit
```

Tkinter comes pre-installed with Python, so no extra installation needed.

---

## 🚀 Usage

1. Clone or download the project:

```bash
git clone https://github.com/ShakalBhau0001/Automation-Using-Python.git
cd WhatsApp-Auto-Messenger
```

2. Run the application:

```bash
python whatsapp_messenger.py
```

3. A GUI window will open — enter:

   - **Phone Number** (with country code, e.g., +91…)  
   - **Your Custom Message**

4. Click **“Send Message”**  
   The app will automatically open WhatsApp Web and send the message.

---

## 🧠 How It Works

- Takes user input for **phone number** and **message**  
- Uses `pywhatkit.sendwhatmsg_instantly()` to send the message  
- Opens WhatsApp Web in the browser  
- Automatically sends your message to the entered number  
- Shows **success** or **error** popups  

---

## 🧑‍💻 Author

Built with ❤️ by **ShakalBhau0001**

---

## ⚙️ Tech Stack

- **Python 3**  
- **Tkinter** — GUI Interface  
- **PyWhatKit** — WhatsApp Automation  

---

> 💬 *"A lightweight tool to send WhatsApp messages instantly with ease and simplicity."*
