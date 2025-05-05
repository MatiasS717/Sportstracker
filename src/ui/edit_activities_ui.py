import tkinter
from tkinter import messagebox
import backend.users_commands
import backend.activities_commands

class EditActivities:
    """Käyttäjän liikuntasuorituksien muokkaamiseen tarkoitettu näkymä."""

    def __init__(self, root, sportstracker, state):
        """Luokan konstruktori. Luo uuden muokkaamisnäkymän.
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
        self._frame = None
        self._state = state
        self.sportstracker = sportstracker

        self.edit_activities_start()

    def _show_error(self, message):
        """Virheviestien näyttäminen."""

        messagebox.showerror(title="Error", message=message)

    def pack(self):
        """Näyttää näkymän."""

        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän."""

        self._frame.destroy()

    def return_command(self):
        """Vie käyttäjän takaisin liikuntasuoritukset-näkymään."""

        self.sportstracker(self._state)

    def delete_activity(self, activity, tracker, training_type):
        """Poistaa liikuntasuorituksen tietokannasta ja päivittää näkymän."""

        result = backend.users_commands.get_id(self._state["session_username"],
        self._state["session_password"])
        user_id = result[0]
        y = 0
        activities = backend.activities_commands.get_activities(user_id)
        for a in activities:
            if activity in a:
                y = 1
        if y == 1:
            backend.activities_commands.delete_activity(activity, tracker, training_type, user_id)
            messagebox.showinfo(title="Activity deleted",
            message="You successfully deleted an activity")
            self.destroy()
            self.edit_activities_start()
            self.pack()
        else:
            self._show_error("Activity allready deleted.")

    def initialize_activity_item(self, activity):
        """Alustaa yksittäisen liikuntasuorituksen näkymään."""

        item_frame = tkinter.Frame(master=self._frame, bg=self.gray)
        list_activity_label = tkinter.Label(master=item_frame, text=activity[1], bg=self.gray,
        fg=self.white, font=("Arial", 14))
        list_tracker_label = tkinter.Label(master=item_frame, text=activity[2], bg=self.gray,
        fg=self.white, font=("Arial", 14))
        list_training_type_label = tkinter.Label(master=item_frame, text=activity[3], bg=self.gray,
        fg=self.white, font=("Arial", 14))
        delete_activity_button = tkinter.Button(master=item_frame, text="Delete",
        bg=self.pink, fg=self.white, font=("Arial", 14),
        command=lambda: self.delete_activity(activity[1], activity[2], activity[3]))

        list_activity_label.grid(row=0, column=0)
        list_tracker_label.grid(row=0, column=1, padx=20)
        list_training_type_label.grid(row=0, column=2)
        delete_activity_button.grid(row=0, column=3, pady=10)

        item_frame.pack()

    def initialize_activity_list(self):
        """Alustaa listan liikuntasuorituksista näkymään."""

        result = backend.users_commands.get_id(self._state["session_username"],
        self._state["session_password"])
        user_id = result[0]
        activities = backend.activities_commands.get_activities(user_id)

        for activity in activities:
            self.initialize_activity_item(activity)

    def initialize_return_button(self):
        """Alustaa painikkeen."""

        button_frame = tkinter.Frame(master=self._frame, bg=self.gray)
        return_button = tkinter.Button(master=button_frame, text="Return to sportstracker",
        bg=self.pink, fg=self.white, font=("Arial", 16), command=self.return_command)
        return_button.grid(row=0, column=1, pady=10)

        button_frame.pack()

    def edit_activities_start(self):
        """Rakentaa näkymän."""

        self._frame = tkinter.Frame(bg=self.gray)

        self.initialize_activity_list()

        self.initialize_return_button()
