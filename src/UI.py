import tkinter
from tkinter import Tk, ttk, constants, messagebox
import sqlite3

class UI:
    def __init__(self, root):
        self._root = root

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        conn = sqlite3.connect('database.db')
        data_get_query = '''SELECT username, password 
                            FROM users
                            WHERE username = ? AND
                            password = ?'''
        cursor = conn.cursor()
        all_results = cursor.execute(data_get_query, [username, password]).fetchall()
        conn.commit()
        conn.close()
        if all_results == []:
            messagebox.showerror(title="Error", message="Invalid login.")
            return
        else:
            result = all_results[0]
        if username==result[0] and password==result[1]:
            messagebox.showinfo(title="Login Success", message="You successfully logged in")
        else:
            messagebox.showerror(title="Error", message="Invalid login.")
    
    def register(self):
        if self.password.get()==self.repeat_password_entry.get():
            username = self.username.get()
            password = self.password.get()
            conn = sqlite3.connect('database.db')
            data_insert_query = '''INSERT INTO users (username, password)
                                   VALUES(?, ?)'''
            data_insert_tuple = (username, password)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
            messagebox.showinfo(title="Register Success", message="You successfully registered")
            self.register_window.destroy()
        else:
            messagebox.showerror(title="Error", message="Invalid register")

    def register_start(self):

        register_window = tkinter.Toplevel()
        self.register_window = register_window
        register_window.title("Sportstracker")
        register_window.geometry('440x340')
        register_window.configure(bg='#333333')

        heading_label = tkinter.Label(register_window, text="Register", bg='#333333', fg="#FFFFFF", font=("Arial", 30))

        username_label = tkinter.Label(register_window, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        username_entry = ttk.Entry(register_window, font=("Arial", 16))
        self.username = username_entry

        password_label = tkinter.Label(register_window, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        password_entry = ttk.Entry(register_window, show="*", font=("Arial", 16))
        self.password = password_entry

        repeat_password_label = tkinter.Label(register_window, text="Repeat password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        repeat_password_entry = ttk.Entry(register_window, show="*", font=("Arial", 16))
        self.repeat_password_entry = repeat_password_entry

        register_button = tkinter.Button(register_window, text="Register", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.register)

        heading_label.grid(row=0, column=0, columnspan=2, pady=40)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=10)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=10)

        repeat_password_label.grid(row=3, column=0)
        repeat_password_entry.grid(row=3, column=1, pady=10)

        register_button.grid(row=4, column=0, columnspan=2, pady=10)

    def start(self):

        frame = tkinter.Frame(bg='#333333')

        heading_label = tkinter.Label(frame, text="Login", bg='#333333', fg="#FFFFFF", font=("Arial", 30))

        username_label = tkinter.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        username_entry = ttk.Entry(frame, font=("Arial", 16))
        self.username_entry = username_entry

        password_label = tkinter.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        password_entry = ttk.Entry(frame, show="*", font=("Arial", 16))
        self.password_entry = password_entry

        login_button = tkinter.Button(frame, text="Log in", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.login)
        register_button = tkinter.Button(frame, text="Register", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.register_start)

        heading_label.grid(row=0, column=0, columnspan=2, pady=40)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=10)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=10)

        login_button.grid(row=3, column=0, columnspan=2, pady=10)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)

        frame.pack()
        



