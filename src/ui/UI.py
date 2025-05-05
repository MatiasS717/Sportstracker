from ui.login_UI import Login
from ui.register_UI import Register
from ui.sportstracker_UI import Sportstracker
from ui.new_activities_ui import NewActivities
from ui.edit_activities_ui import EditActivities

class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.
        Args:
            root:
                TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
            current_view:
                Nykyinen näkymä."""
        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän."""

        self._show_login_view()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän."""

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        """Näyttää sisäänkirjautumis-näkymän."""

        self._hide_current_view()

        self._current_view = Login(
            self._root,
            self._show_sportstracker_view,
            self._show_register_view
        )
        self._current_view.pack()

    def _show_sportstracker_view(self, state):
        """Näyttää näkymän, jossa on liikuntasuoritukset."""

        self._hide_current_view()

        self._current_view = Sportstracker(self._root, self._show_new_activities_view, self._show_edit_activities_view, state)

        self._current_view.pack()

    def _show_register_view(self):
        """Näyttää rekisteröitymis-näkymän."""

        self._hide_current_view()

        self._current_view = Register(
            self._root,
            self._show_login_view
        )
        self._current_view.pack()
    
    def _show_new_activities_view(self, state):
        """Näyttää näkymän, jossa voi lisätä uusia liikuntasuorituksia."""

        self._hide_current_view()

        self._current_view = NewActivities(self._root, self._show_sportstracker_view, state)

        self._current_view.pack()

    def _show_edit_activities_view(self, state):
        """Näyttää näkymän, jossa voi muokata omia liikuntasuorituksia."""

        self._hide_current_view()

        self._current_view = EditActivities(self._root, self._show_sportstracker_view, state)

        self._current_view.pack()
