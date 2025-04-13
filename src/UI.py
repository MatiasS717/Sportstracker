import tkinter
from tkinter import Tk, ttk, constants, messagebox
import sqlite3
import users_commands
import activities_commands
from register_UI import Register
from sportstracker_UI import Sportstracker

# ui
# - view
# - logic
# backend
# - db
# - logic

class UI:
    def __init__(self, root):
        self._root = root
        self.white = "#FFFFFF"
        self.gray = "#333333"
        self.pink = "#FF3399"
        self._state = {}
        self.register = Register(self._state)
        self.sportstracker = Sportstracker(self._state)
        
        
    def _init_view(self, windowname):
        windowname = tkinter.Toplevel()
        windowname.title("Sportstracker") 
        windowname.geometry('440x340')
        windowname.configure(bg=self.gray)

        return windowname

    def _show_error(self, message):
        messagebox.showerror(title="Error", message=message)

    def login(self):
        session_username = self.login_username_entry.get()
        session_password = self.login_password_entry.get()
        self._state["session_username"] = session_username
        self._state["session_password"] = session_password

        result = users_commands.login(session_username, session_password)
        if result == None:
            self._show_error("Invalid login.")
            return
        if session_username==result[0] and session_password==result[1]:
            messagebox.showinfo(title="Login Success", message="You successfully logged in")
            self.sportstracker_start()
        else:
            self._show_error("Invalid login.")

    def sportstracker_start(self):

        self.sportstracker.sportstracker_start()

    def register_start(self):

        self.register.register_start()

    def start(self):

        frame = tkinter.Frame(bg=self.gray)

        heading_label = tkinter.Label(frame, text="Login", bg=self.gray, fg=self.white, font=("Arial", 30))

        username_label = tkinter.Label(frame, text="Username", bg=self.gray, fg=self.white, font=("Arial", 16))
        username_entry = ttk.Entry(frame, font=("Arial", 16))
        self.login_username_entry = username_entry

        password_label = tkinter.Label(frame, text="Password", bg=self.gray, fg=self.white, font=("Arial", 16))
        password_entry = ttk.Entry(frame, show="*", font=("Arial", 16))
        self.login_password_entry = password_entry

        login_button = tkinter.Button(frame, text="Log in", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.login)
        register_button = tkinter.Button(frame, text="Register", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.register_start)

        heading_label.grid(row=0, column=0, columnspan=2, pady=40)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=10)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=10)

        login_button.grid(row=3, column=0, columnspan=2, pady=10)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)

        frame.pack()
