# 📱 PhoneTracer

A simple and clean GUI tool to **trace detailed information about any phone number** using  
**Python + Tkinter + phonenumbers**.  
Just enter a valid number → click **Trace Number** → and all details appear instantly in the app.

---

## ✨ Features

- 🖥️ Easy-to-use Tkinter GUI  
- 🌍 Detects **Country & Region**  
- 📡 Fetches **Carrier / SIM Provider**  
- 🕒 Shows **Timezones** for the number  
- ✔️ Validity check (valid / invalid)  
- ⚠️ Error handling for wrong number formats  
- 🔄 Clear button to reset fields  
- 🎨 Clean and minimal UI  

---

## 📂 Project Structure

```bash
Phone-Tracer/
│
├── phone_tracer.py        # Main application
└── README.md              # Project documentation
```

---

## 🧰 Requirements

Make sure you have **Python 3.7+** or higher.

Install the required dependency:

```bash
pip install phonenumbers
```

Tkinter already comes with Python — no extra installation needed.

---

## 🚀 Usage

1. Clone or download the repository:

```bash
git clone https://github.com/ShakalBhau0001/Automation-Using-Python.git
cd Phone-Tracer
```

2. Run the tool:

```bash
python phone_tracer.py
```

A graphical window will open automatically.

---

## 🧠 How It Works

- Takes the phone number input (with country code)  
- Validates the number using `phonenumbers.is_valid_number()`  
- Extracts:
  - Country  
  - Region  
  - Carrier  
  - Timezones  
- Displays everything neatly in the GUI  
- Handles formatting errors using `NumberParseException`  
- “Clear” button resets input + output instantly  

---

## 📌 Example Input

```
+91XXXXXXXXXX
```

Enter → Click **Trace Number** → Get full details.

---

## 📜 License

This project is free to use for learning and personal automation tasks.

---

## 💛 Author

> Built with ❤️ by **ShakalBhau0001**
