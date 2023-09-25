import tkinter as tk
from abc import ABC, abstractclassmethod

class Game_Setup(ABC):
    CONFIGS = {
        'c1' : '#6F61C0',
        'c2' : '#A084E8',
        'c3' : '#8BE8E5',
        'c4' : '#D5FFE4',
        'font' : ['Consolas', 14, 'bold']
    }
    def __init__(self, main_window, images):
        self.main_window = main_window
        self.images = images
        self.class_window = tk.Toplevel()
        self.class_window.config(bg=self.CONFIGS['c1'])
        self.class_window.geometry('450x600')
        self.class_window.resizable(False, False)
        self.class_window.protocol('WM_DELETE_WINDOW', self._on_close)
    @abstractclassmethod
    def _Restart(self):
        pass
    def _on_close(self):
        self.class_window.destroy()
        self.main_window.destroy()
    def _Exit_game(self):
        self.class_window.destroy()
        self.main_window.deiconify()