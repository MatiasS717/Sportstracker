from tkinter import Tk
from UI import UI


def main():
    window = Tk()
    window.title("Sportstracker")
    window.geometry('440x340')
    window.configure(bg='#333333')

    ui_view = UI(window)
    ui_view.start()
    window.mainloop()

if __name__ == "__main__":
    main()
