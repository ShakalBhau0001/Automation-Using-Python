import tkinter as tk
from tkinter import messagebox
import webbrowser
import urllib.request


def open_site(event=None):
    name = entry.get().strip().lower()
    domain = domain_var.get()

    if not name:
        messagebox.showwarning("Input Error", "Please enter a website name.")
        return

    url = f"https://www.{name}{domain}"
    status_label.config(text="Checking website...", fg="blue")

    try:
        urllib.request.urlopen(url, timeout=5)
        webbrowser.open_new(url)
        status_label.config(text=f"Opened: {url}", fg="green")
    except Exception:
        msg = f"❌ '{name}{domain}' not found.\nSearching on Google..."
        status_label.config(text=msg, fg="red")
        webbrowser.open_new(f"https://www.google.com/search?q={name}")


root = tk.Tk()
root.title("Website Launcher")
root.geometry("420x220")
root.resizable(False, False)
root.configure(bg="#F5F6FA")

title_label = tk.Label(
    root, text="Website Launcher", font=("Arial", 16, "bold"), bg="#F5F6FA"
)
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#F5F6FA")
frame.pack()

entry = tk.Entry(frame, width=28, font=("Arial", 12))
entry.grid(row=0, column=0, padx=5)
entry.insert(0, "google  |  facebook  |  amazon")


def clear_placeholder(event):
    if entry.get().startswith("google"):
        entry.delete(0, tk.END)


entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<Return>", open_site)

domain_var = tk.StringVar(value=".com")
domain_menu = tk.OptionMenu(frame, domain_var, ".com", ".in", ".org", ".net", ".io")
domain_menu.grid(row=0, column=1, padx=5)
domain_menu.config(font=("Arial", 11))

btn = tk.Button(
    root,
    text="Launch Website",
    command=open_site,
    font=("Arial", 13, "bold"),
    bg="#4CAF50",
    fg="white",
    width=16,
)
btn.pack(pady=15)

status_label = tk.Label(root, text="", font=("Arial", 11), bg="#F5F6FA")
status_label.pack()

root.mainloop()
