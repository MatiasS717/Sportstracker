import tkinter
from tkinter import Tk, ttk, constants, messagebox
import users_commands
import activities_commands

class Activities:
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

    def add_activity(self):
        result = users_commands.get_id(self._state["session_username"], self._state["session_password"])
        user_id = result[0]
        activity = self.activity_entry.get()
        tracker = self.tracker_entry.get()
        training_type = self.training_type_entry.get()
        activities_commands.add_activity(activity, tracker, training_type, user_id)
        messagebox.showinfo(title="Activity added", message="You successfully added an activity")


    def activities_start(self):

        activities_window = self._init_view("activities_window")
        activities_window.geometry('840x340')
        
        activities_frame = tkinter.LabelFrame(activities_window, text="Activities")
        activities_frame.grid(row=0, column=0, padx=20, pady=20)

        activity_label = tkinter.Label(activities_frame, text="Activity", font=("Arial", 16))
        activity_entry = ttk.Entry(activities_frame)
        self.activity_entry = activity_entry

        tracker_label = tkinter.Label(activities_frame, text="Tracker", font=("Arial", 16))
        tracker_spinbox = ttk.Spinbox(activities_frame, from_=0, to=1000)
        self.tracker_entry = tracker_spinbox
        
        training_type_label = tkinter.Label(activities_frame, text="Training type", font=("Arial", 16))
        training_type_combobox = ttk.Combobox(activities_frame, values=["", "Endurance", "Strength", "Mobility", "Fitness"])
        self.training_type_entry = training_type_combobox

        add_activity_button = tkinter.Button(activities_window, text="Add activity", bg=self.pink, fg=self.white, font=("Arial", 16), command=self.add_activity)

        activity_label.grid(row=0, column=0)
        activity_entry.grid(row=1, column=0, padx=10)

        tracker_label.grid(row=0, column=1)
        tracker_spinbox.grid(row=1, column=1, padx=10)

        training_type_label.grid(row=0, column=2)
        training_type_combobox.grid(row=1, column=2, padx=10)

        add_activity_button.grid(row=2, column=0, pady=10)
