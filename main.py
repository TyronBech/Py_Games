import tkinter as tk # Importing tkinter to create a window for the program
from dict_images import resized_images # Importing the resized_images to get the resized image
import RPS as rps # Importing the rock_paper_scissors class
import TTT as ttt # Importing the tic_tac_toe class

# The function Game_start() is going to call the class based on type
# of game user wants to open
def Game_start(type):
    window.withdraw()
    if type == 1:
        RPS_Game = rps.rock_paper_scissors(window, images)
    elif type == 2:
        TTT_game = ttt.tic_tac_toe(window, images)

# This function is used to destroy the window once user exit the program
def on_close():
    window.destroy()

# This is the main function of the window, it started all in here.
# It contains the basic structure of the window like size, color, title, labels,
# frame, buttons, and protocol
if __name__ == '__main__':
    # Instance of the window
    window = tk.Tk()
    # Window main title
    window.title('Mini Games')
    # Color (Purple)
    window.config(bg='#6F61C0')
    # size in lengthXheight then resizable to False to avoid resizing the window
    window.geometry('450x600')
    window.resizable(False, False)
    images = resized_images()
    # Icon of the window, the image file is located at Images folder
    # the images dictionary is located in dict_images.py
    window.iconphoto(True, images['mg_icon'])
    # Image title
    Title_label = tk.Label(window, image=images['Title'], bg='#6F61C0')
    Title_label.pack(pady=20)
    # Frame to store the buttons
    button_frame = tk.Frame(window, bg='#6F61C0', width=180, height=300)
    button_frame.pack(pady=30)
    # Button to call the Rock-Paper-Scissor class
    RPS_button = tk.Button(
        button_frame, image=images['RPS'], bg='#6F61C0', borderwidth=0, activebackground='#6F61C0', command=lambda: Game_start(1))
    RPS_button.grid(row=0, column=0, pady=5)
    # Button to call the Tic-Tac-Toe class
    TTT_button = tk.Button(
        button_frame, image=images['TTT'], bg='#6F61C0', borderwidth=0, activebackground='#6F61C0', command=lambda: Game_start(2))
    TTT_button.grid(row=1, column=0, pady=5)
    # Once user press the x button on the top right of the window,
    # it will call the on_close() to fully destroy the window
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()
