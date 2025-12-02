## 🌐 Website Launcher
A clean and simple GUI application that lets you open any website instantly using **Python + Tkinter**.
Just type a website name → choose a domain → click **Launch Website** → and it opens in your browser.
If the website doesn't exist, it automatically **searches it on Google**.

---

## ✨ Features

- 🚀 Open any website with one click
- 🎯 Auto-detect full URLs (with https://)
- 🌍 Domain selector (.com, .in, .net, .org, .io, etc.)
- 🔎 Auto Google Search if website not found
- 🖥️ Clean and modern Tkinter GUI
- ⚡ Fast, lightweight, and beginner-friendly
- 📶 No installation required — works offline (except browser opening)

---

## 📂 Project Structure

```bash
Website-Launcher/
│
├── website_launcher.py   # Main application
└── README.md             # Project documentation
```

---

## ⚙️ Tech Stack

- **Python 3**
- **Tkinter** — GUI Interface
- **urllib.request** — Website checking
- **webbrowser** — Opens website in the default browser

---

## 🧰 Requirements

Make sure you have **Python 3.7+** installed.
No extra libraries are needed — Tkinter, urllib, and webbrowser come with Python.

---

## 🚀 Usage

1. Clone or download this project:
```bash
git clone https://github.com/ShakalBhau0001/Automation-Using-Python.git
cd Website-Launcher
```
  
2. Run the application:
```bash
python website_launcher.py
```
  
3. A GUI window will open — enter:
- **Website name** (example: google, facebook, amazon)
- Or a **full URL** (https://example.com)

4. Choose the domain (.com, .in, .org, .net…) if needed
5. Click “**Launch Website**”
6. If the website exists → it opens
7. If not → the app automatically **searches it on Google**

---

## 🧠 How It Works

- Takes the website name or URL from the input box
- Builds a full URL like `https://www.example.com`
- Uses `urllib.request` to verify if the site exists
- If valid → opens it using the default web browser
- If invalid → sends a Google search query automatically

---

> 🌐 "Open any website instantly — smart, clean, and simple."

---

## 🧑‍💻 Author

Built with ❤️ by **ShakalBhau0001**

---
