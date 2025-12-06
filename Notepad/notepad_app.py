import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk


class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("900x650")

        self.current_file = None
        self.dark_mode = False
        self.font_size = 14
        self.last_saved_text = ""

        self.create_widgets()
        self.create_menu()
        self.create_status_bar()
        self.bind_shortcuts()

        self.auto_save()
        self.update_all()

    # GUI ELEMENTS
    def create_widgets(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        # Line Numbers
        self.line_numbers = tk.Text(
            main_frame,
            width=4,
            padx=4,
            takefocus=0,
            border=0,
            background="#f0f0f0",
            state="disabled",
        )
        self.line_numbers.pack(side="left", fill="y")

        # Text Area
        self.text_area = scrolledtext.ScrolledText(
            main_frame, font=("Consolas", self.font_size), undo=True
        )
        self.text_area.pack(side="right", fill="both", expand=True)

        # Single key binding for everything
        self.text_area.bind("<KeyRelease>", self.update_all)

    # MENU
    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=False)
        file_menu.add_command(label="New (Ctrl+N)", command=self.new_file)
        file_menu.add_command(label="Open (Ctrl+O)", command=self.open_file)
        file_menu.add_command(label="Save (Ctrl+S)", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit Menu
        edit_menu = tk.Menu(menu_bar, tearoff=False)
        edit_menu.add_command(
            label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>")
        )
        edit_menu.add_command(
            label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>")
        )
        edit_menu.add_command(
            label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>")
        )
        edit_menu.add_command(
            label="Search & Replace (Ctrl+F)", command=self.search_replace_window
        )
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # View Menu
        view_menu = tk.Menu(menu_bar, tearoff=False)
        view_menu.add_command(label="Dark Mode", command=self.toggle_dark_mode)

        font_menu = tk.Menu(view_menu, tearoff=False)
        font_menu.add_command(
            label="Increase Font (+)", command=lambda: self.change_font_size(1)
        )
        font_menu.add_command(
            label="Decrease Font (-)", command=lambda: self.change_font_size(-1)
        )
        view_menu.add_cascade(label="Font Size", menu=font_menu)

        menu_bar.add_cascade(label="View", menu=view_menu)
        self.root.config(menu=menu_bar)

    # STATUS BAR
    def create_status_bar(self):
        self.status = tk.Label(self.root, text="Words: 0", anchor="w")
        self.status.pack(side="bottom", fill="x")

    # FILE FUNCTIONS
    def new_file(self):
        self.current_file = None
        self.text_area.delete("1.0", tk.END)
        self.update_all()

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert(tk.END, f.read())
                self.current_file = path
                self.update_all()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def save_file(self):
        if not self.current_file:
            self.save_as_file()
            return

        try:
            with open(self.current_file, "w", encoding="utf-8") as f:
                text = self.text_area.get("1.0", tk.END)
                f.write(text)
                self.last_saved_text = text
            self.status.config(text=f"Saved | Words: {self.count_words(text)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_as_file(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if path:
            self.current_file = path
            self.save_file()

    # AUTO SAVE
    def auto_save(self):
        current_text = self.text_area.get("1.0", tk.END)

        if self.current_file and current_text != self.last_saved_text:
            try:
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(current_text)
                self.last_saved_text = current_text
            except:
                pass

        self.root.after(10000, self.auto_save)

    # LINE NUMBERS
    def update_line_numbers(self):
        lines = self.text_area.get("1.0", "end").count("\n")
        nums = "\n".join(str(i) for i in range(1, lines))

        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", "end")
        self.line_numbers.insert("1.0", nums)
        self.line_numbers.config(state="disabled")

    # WORD COUNT
    def count_words(self, text):
        return len([w for w in text.split() if w.strip()])

    def update_word_count(self):
        text = self.text_area.get("1.0", "end-1c")
        words = self.count_words(text)
        self.status.config(text=f"Words: {words}")

    # Combined Updater
    def update_all(self, event=None):
        self.update_word_count()
        self.update_line_numbers()

    # FONT SIZE
    def change_font_size(self, diff):
        self.font_size += diff
        self.text_area.config(font=("Consolas", self.font_size))

    # SEARCH & REPLACE
    def search_replace_window(self):
        win = tk.Toplevel(self.root)
        win.title("Search & Replace")
        win.geometry("300x150")

        tk.Label(win, text="Find:").pack()
        find_entry = tk.Entry(win)
        find_entry.pack(fill="x")

        tk.Label(win, text="Replace:").pack()
        replace_entry = tk.Entry(win)
        replace_entry.pack(fill="x")

        def replace_all():
            find = find_entry.get()
            replace = replace_entry.get()
            content = self.text_area.get("1.0", tk.END)
            new_content = content.replace(find, replace)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, new_content)
            win.destroy()

        tk.Button(win, text="Replace All", command=replace_all).pack(pady=10)

    # DARK MODE
    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.text_area.config(bg="#1e1e1e", fg="white", insertbackground="white")
            self.line_numbers.config(bg="#2a2a2a", fg="white")
        else:
            self.text_area.config(bg="white", fg="black", insertbackground="black")
            self.line_numbers.config(bg="#f0f0f0", fg="black")

    # SHORTCUTS
    def bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-f>", lambda e: self.search_replace_window())


# MAIN
if __name__ == "__main__":
    root = tk.Tk()
    NotepadApp(root)
    root.mainloop()
