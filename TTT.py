import tkinter as tk
import main as mn
import random

class tic_tac_toe(object):
    def __init__(self, main_window, images):
        self.images = images
        self.class_window = tk.Toplevel()
        self.class_window.config(bg=mn.COLORS[1])
        self.class_window.geometry('450x600')
        self.class_window.resizable(False, False)
        self.class_window.protocol('WM_DELETE_WINDOW', lambda: self._on_close(main_window))
        self.TTT_title = tk.Label(self.class_window, image=self.images['TTT_title'], bg=mn.COLORS[1])
        self.TTT_title.pack()
        self._Buttons()
    def _on_close(self, main_window):
        self.class_window.destroy()
        main_window.deiconify()