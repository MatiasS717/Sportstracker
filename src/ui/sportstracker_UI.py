import tkinter
from tkinter import Tk, ttk, constants, messagebox
import backend.users_commands
import backend.activities_commands

class Sportstracker:
    """Käyttäjän liikuntasuorituksien näkemiseen tarkoitettu näkymä."""

    def __init__(self, root, new_activities, edit_activities, state):
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
                new_activities:
                    Uusien liikuntasuoritusten lisäämiseen tarkoitettu näkymä.
                edit_activities:
                    Liikuntasuoritusten muokkaamiseen tarkoitettu näkymä.
        """

        self._root = root
        self.white = "#FFFFFF"
        self.gray = "#333333"
        self.pink = "#FF3399"
        self._state = state
        self._frame = None
        self.new_activities = new_activities
        self.edit_activities = edit_activities

        self.sportstracker_start()

    def pack(self):
        """Näyttää näkymän."""

        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän."""

        self._frame.destroy()

    def new_activities_start(self):
        """Käynnistää uusien liikuntasuoritusten lisäämiseen tarkoitetun näkymän."""

        self.new_activities(self._state)
    
    def edit_activities_start(self):
        """Käynnistää liikuntasuoritusten muokkaamiseen tarkoitetun näkymän."""

        self.edit_activities(self._state)

    def sportstracker_start(self):
        """Rakentaa näkymän."""

        self._frame = tkinter.Frame(bg=self.gray)

        heading_label = tkinter.Label(self._frame, text="Sportstracker", bg=self.gray, fg=self.white, font=("Arial", 20))
        user_label = tkinter.Label(self._frame, text="User:", bg=self.gray, fg=self.white, font=("Arial", 16))
        activities_label = tkinter.Label(self._frame, text="Activities", bg=self.gray, fg=self.pink, font=("Arial", 16))
        activity_label = tkinter.Label(self._frame, text="Activity", bg=self.gray, fg=self.white, font=("Arial", 16))
        tracker_label = tkinter.Label(self._frame, text="Tracker", bg=self.gray, fg=self.white, font=("Arial", 16))
        training_type_label = tkinter.Label(self._frame, text="Training type", bg=self.gray, fg=self.white, font=("Arial", 16))

        heading_label.grid(row=0, column=0)
        user_label.grid(row=1, column=0)
        activities_label.grid(row=2, column=1)
        activity_label.grid(row=3, column=0)
        tracker_label.grid(row=3, column=1)
        training_type_label.grid(row=3, column=2)

        username_label = tkinter.Label(self._frame, text=self._state["session_username"], bg=self.gray, fg=self.white, font=("Arial", 16))
        username_label.grid(row=1, column=1)

        result = backend.users_commands.get_id(self._state["session_username"], self._state["session_password"])
        user_id = result[0]
        activities = backend.activities_commands.get_activities(user_id)
        x = 4

        for activity in activities:
            list_activity_label = tkinter.Label(self._frame, text=activity[1], bg=self.gray, fg=self.white, font=("Arial", 14))
            list_tracker_label = tkinter.Label(self._frame, text=activity[2], bg=self.gray, fg=self.white, font=("Arial", 14))
            list_training_type_label = tkinter.Label(self._frame, text=activity[3], bg=self.gray, fg=self.white, font=("Arial", 14))

            list_activity_label.grid(row=x, column=0)
            list_tracker_label.grid(row=x, column=1)
            list_training_type_label.grid(row=x, column=2)

            x += 1
        
        new_activity_button = tkinter.Button(self._frame, text="New activity", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.new_activities_start)
        new_activity_button.grid(row=x, column=1, pady=10)

        edit_activities_button = tkinter.Button(self._frame, text="Edit activities", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.edit_activities_start)
        edit_activities_button.grid(row=(x+1), column=1, pady=10)
        