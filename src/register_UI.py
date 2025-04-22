import tkinter
from tkinter import Tk, ttk, constants, messagebox
import sqlite3
import users_commands

class Register:
    """Rekisteröitymiseen tarkoitettu näkymä."""

    def __init__(self, root, login):
        """Luokan konstruktori. Luo uuden liikuntasuoritukset-näkymän.

            Args:
                root:
                    TKinter-elementti, jonka sisään näkymä alustetaan.
                white, gray, pink:
                    TKinter värejä.
                frame:
                    Näkymän kehys.
                login:
                    Sisäänkirjautumisen näkymä.
        """

        self._root = root
        self.white = "#FFFFFF"
        self.gray = "#333333"
        self.pink = "#FF3399"
        self.login = login
        self._frame = None

        self.register_start()

    def pack(self):
        """Näyttää näkymän."""

        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän."""

        self._frame.destroy()

    def _show_error(self, message):
        """Virheviestien näyttäminen."""

        messagebox.showerror(title="Error", message=message)

    def register_command(self):
        """Luo uuden käyttäjän tietokantaan."""

        if self.register_password_entry.get()==self.register_repeat_password_entry.get():
            username = self.register_username_entry.get()
            password = self.register_password_entry.get()
            try:
                users_commands.register(username, password)
                messagebox.showinfo(title="Register Success", message="You successfully registered")
                self.login()
            except sqlite3.IntegrityError:
                self._show_error("Username allready taken")
        else:
            self._show_error("Passwords do not match")

    def register_start(self):
        """Rakentaa näkymän."""

        self._frame = tkinter.Frame(bg=self.gray)

        heading_label = tkinter.Label(self._frame, text="Register", bg=self.gray, fg=self.white, font=("Arial", 30))

        username_label = tkinter.Label(self._frame, text="Username", bg=self.gray, fg=self.white, font=("Arial", 16))
        username_entry = ttk.Entry(self._frame, font=("Arial", 16))
        self.register_username_entry = username_entry

        password_label = tkinter.Label(self._frame, text="Password", bg=self.gray, fg=self.white, font=("Arial", 16))
        password_entry = ttk.Entry(self._frame, show="*", font=("Arial", 16))
        self.register_password_entry = password_entry

        repeat_password_label = tkinter.Label(self._frame, text="Repeat password", bg=self.gray, fg=self.white, font=("Arial", 16))
        repeat_password_entry = ttk.Entry(self._frame, show="*", font=("Arial", 16))
        self.register_repeat_password_entry = repeat_password_entry

        register_button = tkinter.Button(self._frame, text="Register", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.register_command)

        heading_label.grid(row=0, column=0, columnspan=2, pady=40)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=10)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=10)

        repeat_password_label.grid(row=3, column=0)
        repeat_password_entry.grid(row=3, column=1, pady=10)

        register_button.grid(row=4, column=0, columnspan=2, pady=10)
