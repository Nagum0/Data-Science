from tkinter import *
from tkinter import ttk

from . import menu

class Main(Tk):
    def __init__(self):
        super().__init__()
        #Window setup
        self.title("Pomodoro App")
        self.geometry("620x480")
        self.resizable(False, False)

        #Added elements
        self.main_menu = menu.Menu()

        #Placing widgets
        self.placeWidgets()

    def placeWidgets(self) -> None:
        self.main_menu.place(x=15, y=15)