import tkinter as tk
from tkinter import ttk, messagebox
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import NumberParseException


def trace_number():
    number = entry_number.get().strip()

    if not number:
        messagebox.showwarning("Warning", "Please enter a phone number.")
        return

    try:
        p = phonenumbers.parse(number, None)
        if not phonenumbers.is_valid_number(p):
            messagebox.showerror("Invalid", "This is not a valid phone number.")
            return

        location = geocoder.description_for_number(p, "en") or "Unknown"
        country = geocoder.country_name_for_number(p, "en") or "Unknown"
        sim_carrier = carrier.name_for_number(p, "en") or "Unknown"
        tz = timezone.time_zones_for_number(p)
        tz_str = ", ".join(tz) if tz else "Unknown"
        result_text.set(
            f"Target      : {number}\n"
            f"Country     : {country}\n"
            f"Region      : {location}\n"
            f"Carrier     : {sim_carrier}\n"
            f"Timezones   : {tz_str}\n"
        )

    except NumberParseException:
        messagebox.showerror("Error", "Enter Mobile Number with Country Code.")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected Error: {e}")


def clear_all():
    entry_number.delete(0, tk.END)
    result_text.set("")


root = tk.Tk()
root.title("PhoneTracer")
root.geometry("450x350")
root.resizable(False, False)

title = ttk.Label(root, text="PhoneTracer", font=("Arial", 20, "bold"))
title.pack(pady=15)

frame = ttk.Frame(root)
frame.pack(pady=10)

label_number = ttk.Label(frame, text="Enter Phone Number:")
label_number.grid(row=0, column=0, padx=5, pady=5)

entry_number = ttk.Entry(frame, width=35)
entry_number.grid(row=0, column=1, padx=5, pady=5)
entry_number.focus()


btn_frame = ttk.Frame(root)
btn_frame.pack(pady=5)

trace_btn = ttk.Button(btn_frame, text="Trace Number", command=trace_number)
trace_btn.grid(row=0, column=0, padx=10)

clear_btn = ttk.Button(btn_frame, text="Clear", command=clear_all)
clear_btn.grid(row=0, column=1, padx=10)

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, font=("Courier New", 12), justify="left")
result_label.pack(pady=15)

root.mainloop()
