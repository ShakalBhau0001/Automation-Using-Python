import pywhatkit as pwk
import tkinter as tk
from tkinter import messagebox


def send_msg():
    number = entry_number.get().strip()
    custom_message = entry_message.get().strip()

    if number == "" or custom_message == "":
        messagebox.showerror("Error", "Please enter phone number and message")
        return

    try:
        pwk.sendwhatmsg_instantly(number, custom_message)
        messagebox.showinfo("Success", "Message sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed: {e}")


root = tk.Tk()
root.title("WhatsApp Auto Messenger")
root.geometry("350x250")

tk.Label(root, text="Phone Number (+91..)").pack(pady=5)
entry_number = tk.Entry(root, width=30)
entry_number.pack()

tk.Label(root, text="Enter Your Message").pack(pady=5)
entry_message = tk.Entry(root, width=30)
entry_message.pack()

tk.Button(root, text="Send Message", command=send_msg, bg="green", fg="white").pack(pady=20)

root.mainloop()
