import tkinter
from tkinter import Tk, ttk, constants, messagebox
import sqlite3
import users_commands

class Login:
    """Sisäänkirjautumiseen tarkoitettu näkymä."""

    def __init__(self, root, sportstracker, register):
        """Luokan konstruktori. Luo uuden liikuntasuoritukset-näkymän.

            Args:
                root:
                    TKinter-elementti, jonka sisään näkymä alustetaan.
                white, gray, pink:
                    TKinter värejä.
                state:
                    Näkymästä toiseen siirtyvät kirjautumistiedot.
                frame:
                    Näkymän kehys.
                sportstracker:
                    Liikuntasuoritukset näyttävä näkymä.
                register:
                    Rekisteröitymisnäkymä.
        """

        self._root = root
        self.white = "#FFFFFF"
        self.gray = "#333333"
        self.pink = "#FF3399"
        self._frame = None
        self._state = {}
        self.sportstracker = sportstracker
        self.register = register

        self.login_start()
        
    def _show_error(self, message):
        """Virheviestien näyttäminen."""

        messagebox.showerror(title="Error", message=message)

    def pack(self):
        """Näyttää näkymän."""

        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän."""

        self._frame.destroy()

    def login_command(self):
        """Hoitaa sisäänkirjautumisen."""

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
            self.sportstracker(self._state)
        else:
            self._show_error("Invalid login.")


    def login_start(self):
        """Rakentaa näkymän."""

        self._frame = tkinter.Frame(bg=self.gray)

        heading_label = tkinter.Label(self._frame, text="Login", bg=self.gray, fg=self.white, font=("Arial", 30))

        username_label = tkinter.Label(self._frame, text="Username", bg=self.gray, fg=self.white, font=("Arial", 16))
        username_entry = ttk.Entry(self._frame, font=("Arial", 16))
        self.login_username_entry = username_entry

        password_label = tkinter.Label(self._frame, text="Password", bg=self.gray, fg=self.white, font=("Arial", 16))
        password_entry = ttk.Entry(self._frame, show="*", font=("Arial", 16))
        self.login_password_entry = password_entry

        login_button = tkinter.Button(self._frame, text="Log in", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.login_command)
        register_button = tkinter.Button(self._frame, text="Register", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.register)

        heading_label.grid(row=0, column=0, columnspan=2, pady=40)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=10)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=10)

        login_button.grid(row=3, column=0, columnspan=2, pady=10)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)

        self._frame.pack()