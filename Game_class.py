import tkinter as tk # Importing tkinter for the window
from abc import ABC, abstractclassmethod # Importing abc to make parent class method abstract

# Abstract parent class
class Game_Setup(ABC):
    # Configurations of the window for color and font
    CONFIGS = {
        'c1': '#6F61C0',
        'c2': '#A084E8',
        'c3': '#8BE8E5',
        'c4': '#D5FFE4',
        'font': ['Consolas', 14, 'bold']
    }
    # Constructor for the parent class where the intance of the window is created
    def __init__(self, main_window, images, icon):
        self.main_window = main_window
        self.images = images
        self.class_window = tk.Toplevel()
        self.class_window.config(bg=self.CONFIGS['c1'])
        self.class_window.geometry('450x600')
        self.class_window.resizable(False, False)
        self.class_window.iconphoto(True, icon)
        self.class_window.protocol('WM_DELETE_WINDOW', self._on_close)
    # Abstract method used for identifying who won in the match
    @abstractclassmethod
    def _identify_winner(self):
        pass
    # Abstract methof to implement a restart function for the game
    @abstractclassmethod
    def _Restart(self):
        pass
    # Medthod used to close the window completely
    def _on_close(self):
        self.class_window.destroy()
        self.main_window.destroy()
    # Method to close the top level window and get back to the main window
    def _Exit_game(self):
        self.class_window.destroy()
        self.main_window.deiconify()
        self.main_window.iconphoto(True, self.images['mg_icon'])