import tkinter
from tkinter import Tk, ttk, constants, messagebox
import sql_commands

class UI:
    def __init__(self, root):
        self._root = root

    def login(self):
        self.session_username = self.login_username_entry.get()
        self.session_password = self.login_password_entry.get()
        result = sql_commands.login(self.session_username, self.session_password)
        if result == None:
            messagebox.showerror(title="Error", message="Invalid login.")
            return
        if self.session_username==result[0] and self.session_password==result[1]:
            messagebox.showinfo(title="Login Success", message="You successfully logged in")
            self.sportstracker_start()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")
    
    def register(self):
        if self.register_password_entry.get()==self.register_repeat_password_entry.get():
            username = self.register_username_entry.get()
            password = self.register_password_entry.get()
            try:
                sql_commands.register(username, password)
                messagebox.showinfo(title="Register Success", message="You successfully registered")
                self.register_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror(title="Error", message="Username allready taken")
        else:
            messagebox.showerror(title="Error", message="Passwords do not match")

    def activities_start(self):

        activities_window = tkinter.Toplevel()
        self.activities_window = activities_window
        activities_window.title("Sportstracker")
        activities_window.geometry('840x340')
        activities_window.configure(bg='#333333')

        activities_frame = tkinter.LabelFrame(activities_window, text="Activities")
        activities_frame.grid(row=0, column=0, padx=20, pady=20)

        activity_label = tkinter.Label(activities_frame, text="Activity", font=("Arial", 16))
        activity_entry = ttk.Entry(activities_frame)

        tracker_label = tkinter.Label(activities_frame, text="Tracker", font=("Arial", 16))
        tracker_spinbox = ttk.Spinbox(activities_frame, from_=0, to=1000)
        
        training_type_label = tkinter.Label(activities_frame, text="Training type", font=("Arial", 16))
        training_type_combobox = ttk.Combobox(activities_frame, values=["", "Endurance", "Strength", "Mobility", "Fitness"])

        activity_label.grid(row=0, column=0)
        activity_entry.grid(row=1, column=0, padx=10)

        tracker_label.grid(row=0, column=1)
        tracker_spinbox.grid(row=1, column=1, padx=10)

        training_type_label.grid(row=0, column=2)
        training_type_combobox.grid(row=1, column=2, padx=10)

    def sportstracker_start(self):

        sportstracker_window = tkinter.Toplevel()
        self.sportstracker_window = sportstracker_window
        sportstracker_window.title("Sportstracker")
        sportstracker_window.geometry('440x340')
        sportstracker_window.configure(bg='#333333')

        heading_label = tkinter.Label(sportstracker_window, text="Sportstracker", bg='#333333', fg="#FFFFFF", font=("Arial", 20))
        user_label = tkinter.Label(sportstracker_window, text="User:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        username_label = tkinter.Label(sportstracker_window, text=self.session_username, bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        activities_label = tkinter.Label(sportstracker_window, text="Activities", bg='#333333', fg="#FF3399", font=("Arial", 16))
        add_activity_button = tkinter.Button(sportstracker_window, text="Add activity", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.activities_start)

        heading_label.grid(row=0, column=0)
        user_label.grid(row=1, column=0)
        username_label.grid(row=1, column=1)
        activities_label.grid(row=2, column=1)
        add_activity_button.grid(row=3, column=1, pady=10)

    def register_start(self):

        register_window = tkinter.Toplevel()
        self.register_window = register_window
        register_window.title("Sportstracker")
        register_window.geometry('440x340')
        register_window.configure(bg='#333333')

        heading_label = tkinter.Label(register_window, text="Register", bg='#333333', fg="#FFFFFF", font=("Arial", 30))

        username_label = tkinter.Label(register_window, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        username_entry = ttk.Entry(register_window, font=("Arial", 16))
        self.register_username_entry = username_entry

        password_label = tkinter.Label(register_window, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        password_entry = ttk.Entry(register_window, show="*", font=("Arial", 16))
        self.register_password_entry = password_entry

        repeat_password_label = tkinter.Label(register_window, text="Repeat password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        repeat_password_entry = ttk.Entry(register_window, show="*", font=("Arial", 16))
        self.register_repeat_password_entry = repeat_password_entry

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
        self.login_username_entry = username_entry

        password_label = tkinter.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        password_entry = ttk.Entry(frame, show="*", font=("Arial", 16))
        self.login_password_entry = password_entry

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
        



