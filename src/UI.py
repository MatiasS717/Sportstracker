from login_UI import Login
from register_UI import Register
from sportstracker_UI import Sportstracker
from new_activities_UI import New_activities
from edit_activities_UI import Edit_activities

# ui
# - view
# - logic
# backend
# - db
# - logic

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = Login(
            self._root,
            self._show_sportstracker_view,
            self._show_register_view
        )
        self._current_view.pack()

    def _show_sportstracker_view(self, state):
        self._hide_current_view()

        self._current_view = Sportstracker(self._root, self._show_new_activities_view, self._show_edit_activities_view, state)

        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()

        self._current_view = Register(
            self._root,
            self._show_login_view
        )
        self._current_view.pack()
    
    def _show_new_activities_view(self, state):
        self._hide_current_view()

        self._current_view = New_activities(self._root, self._show_sportstracker_view, state)

        self._current_view.pack()

    def _show_edit_activities_view(self, state):
        self._hide_current_view()

        self._current_view = Edit_activities(self._root, self._show_sportstracker_view, state)

        self._current_view.pack()
