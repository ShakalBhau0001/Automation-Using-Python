# import pywhatkit as pwk
# import tkinter as tk
# from tkinter import messagebox


# def send_msg():
#     number = entry_number.get().strip()
#     custom_message = entry_message.get().strip()

#     if number == "" or custom_message == "":
#         messagebox.showerror("Error", "Please enter phone number and message")
#         return

#     try:
#         pwk.sendwhatmsg_instantly(number, custom_message)
#         messagebox.showinfo("Success", "Message sent successfully!")
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed: {e}")


# root = tk.Tk()
# root.title("WhatsApp Auto Messenger")
# root.geometry("350x250")

# tk.Label(root, text="Phone Number (+91..)").pack(pady=5)
# entry_number = tk.Entry(root, width=30)
# entry_number.pack()

# tk.Label(root, text="Enter Your Message").pack(pady=5)
# entry_message = tk.Entry(root, width=30)
# entry_message.pack()

# tk.Button(root, text="Send Message", command=send_msg, bg="green", fg="white").pack(pady=20)

# root.mainloop()


import tkinter as tk
from tkinter import messagebox
import webbrowser
import urllib.parse


def send_msg():
    number = entry_number.get().strip()
    message = entry_message.get().strip()

    if not number or not message:
        messagebox.showerror("Error", "Both phone number and message are required.")
        return

    if not number.startswith("+"):
        messagebox.showerror(
            "Error", "Phone number must include country code (e.g. +91XXXXXXXXXX)."
        )
        return

    encoded_message = urllib.parse.quote(message)
    url = f"https://web.whatsapp.com/send?phone={number}&text={encoded_message}"

    try:
        webbrowser.open(url)
        messagebox.showinfo(
            "Info",
            "WhatsApp Web has been opened.\nPlease press the Send button manually.",
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI
root = tk.Tk()
root.title("WhatsApp Messenger")
root.geometry("400x270")
root.resizable(False, False)

tk.Label(
    root, text="Phone Number (with country code)", font=("Arial", 10, "bold")
).pack(pady=6)

entry_number = tk.Entry(root, width=38)
entry_number.pack()

tk.Label(root, text="Message", font=("Arial", 10, "bold")).pack(pady=6)

entry_message = tk.Entry(root, width=38)
entry_message.pack()

tk.Button(
    root,
    text="Open WhatsApp",
    command=send_msg,
    bg="#25D366",
    fg="white",
    font=("Arial", 10, "bold"),
    width=22,
).pack(pady=22)

root.mainloop()
