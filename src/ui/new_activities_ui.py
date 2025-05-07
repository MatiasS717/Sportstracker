import tkinter
from tkinter import ttk, messagebox
import backend.users_commands
import backend.activities_commands

class NewActivities:
    """Käyttäjän uusien liikuntasuoritusten lisäämiseen tarkoitettu näkymä."""

    def __init__(self, root, sportstracker, state):
        """Luokan konstruktori. Luo uuden lisäämisnäkymän.
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
                    Liikuntasuoritukset näyttävän näkymän funktio.
        """
        self._root = root
        self.white = "#FFFFFF"
        self.gray = "#333333"
        self.pink = "#FF3399"
        self._state = state
        self._frame = None
        self.sportstracker = sportstracker

        self.new_activities_start()

    def _show_error(self, message):
        """Virheviestien näyttäminen."""

        messagebox.showerror(title="Error", message=message)

    def pack(self):
        """Näyttää näkymän."""

        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän."""

        self._frame.destroy()

    def add_activity(self, activity, tracker, training_type):
        """Lisää uuden liikuntasuorituksen tietokantaan."""

        result = backend.users_commands.get_id(self._state["session_username"],
        self._state["session_password"])
        user_id = result[0]
        activities = backend.activities_commands.get_activities(user_id)
        y = 0
        if activity == "" or tracker == "" or training_type == "":
            self._show_error("Please fill out all the entries.")
        else:
            for a in activities:
                if activity in a:
                    y = 1
            if y == 0:
                backend.activities_commands.add_activity(activity, tracker,
                training_type, user_id)
                messagebox.showinfo(title="Activity added",
                message="You successfully added an activity")
            else:
                self._show_error("Activity allready exists.")

    def return_command(self):
        """Vie käyttäjän takaisin liikuntasuoritukset-näkymään."""

        self.sportstracker(self._state)

    def new_activities_start(self):
        """Rakentaa näkymän."""

        self._frame = tkinter.Frame(bg=self.gray)

        activities_frame = tkinter.LabelFrame(self._frame, text="Activities")
        activities_frame.grid(row=0, column=0, padx=20, pady=20)

        activity_label = tkinter.Label(activities_frame, text="Activity", font=("Arial", 16))
        activity_entry = ttk.Entry(activities_frame)

        tracker_label = tkinter.Label(activities_frame, text="Tracker", font=("Arial", 16))
        tracker_spinbox = ttk.Spinbox(activities_frame, from_=0, to=1000)

        training_type_label = tkinter.Label(activities_frame,
        text="Training type", font=("Arial", 16))
        training_type_combobox = ttk.Combobox(activities_frame,
        values=["", "Endurance", "Strength", "Mobility", "Fitness"])

        add_activity_button = tkinter.Button(self._frame, text="Add activity",
        bg=self.pink, fg=self.white, font=("Arial", 16),
        command=lambda: self.add_activity(activity_entry.get(), tracker_spinbox.get(),
        training_type_combobox.get()))
        return_button = tkinter.Button(self._frame, text="Return to sportstracker",
        bg=self.pink, fg=self.white, font=("Arial", 16), command=self.return_command)

        activity_label.grid(row=0, column=0)
        activity_entry.grid(row=1, column=0, padx=10)

        tracker_label.grid(row=0, column=1)
        tracker_spinbox.grid(row=1, column=1, padx=10)

        training_type_label.grid(row=0, column=2)
        training_type_combobox.grid(row=1, column=2, padx=10)

        add_activity_button.grid(row=2, column=0, pady=10)
        return_button.grid(row=3, column=0, pady=10)
