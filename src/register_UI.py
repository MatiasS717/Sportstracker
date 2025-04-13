import tkinter
from tkinter import Tk, ttk, constants, messagebox
import sqlite3
import users_commands

class Register:
    def __init__(self, state):
        self.white = "#FFFFFF"
        self.gray = "#333333"
        self.pink = "#FF3399"
        self._state = state
        
    def _init_view(self, windowname):
        windowname = tkinter.Toplevel()
        windowname.title("Sportstracker")
        windowname.geometry('440x340')
        windowname.configure(bg=self.gray)

        return windowname

    def _show_error(self, message):
        messagebox.showerror(title="Error", message=message)

    def register_command(self):
        if self.register_password_entry.get()==self.register_repeat_password_entry.get():
            username = self.register_username_entry.get()
            password = self.register_password_entry.get()
            try:
                users_commands.register(username, password)
                messagebox.showinfo(title="Register Success", message="You successfully registered")
                self.register_window.destroy()
            except sqlite3.IntegrityError:
                self._show_error("Username allready taken")
        else:
            self._show_error("Passwords do not match")

    def register_start(self):

        register_window = self._init_view("register_window")
        self.register_window = register_window

        heading_label = tkinter.Label(register_window, text="Register", bg=self.gray, fg=self.white, font=("Arial", 30))

        username_label = tkinter.Label(register_window, text="Username", bg=self.gray, fg=self.white, font=("Arial", 16))
        username_entry = ttk.Entry(register_window, font=("Arial", 16))
        self.register_username_entry = username_entry

        password_label = tkinter.Label(register_window, text="Password", bg=self.gray, fg=self.white, font=("Arial", 16))
        password_entry = ttk.Entry(register_window, show="*", font=("Arial", 16))
        self.register_password_entry = password_entry

        repeat_password_label = tkinter.Label(register_window, text="Repeat password", bg=self.gray, fg=self.white, font=("Arial", 16))
        repeat_password_entry = ttk.Entry(register_window, show="*", font=("Arial", 16))
        self.register_repeat_password_entry = repeat_password_entry

        register_button = tkinter.Button(register_window, text="Register", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.register_command)

        heading_label.grid(row=0, column=0, columnspan=2, pady=40)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=10)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=10)

        repeat_password_label.grid(row=3, column=0)
        repeat_password_entry.grid(row=3, column=1, pady=10)

        register_button.grid(row=4, column=0, columnspan=2, pady=10)
