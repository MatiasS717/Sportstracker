from tkinter import Tk
from ui.UI import UI


def main():
    """Asettaa ikkunan asetukset ja käynnistää UI:n alustaman ikkunan."""

    window = Tk()
    window.title("Sportstracker")
    window.geometry('640x340')
    window.configure(bg='#333333')

    ui_view = UI(window)
    ui_view.start()
    window.mainloop()

if __name__ == "__main__":
    main()
