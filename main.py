import tkinter as tk
from dict_images import resized_images
import RPS as rps
import TTT as ttt

def Game_start(type):
        window.withdraw()
        if type == 1:
            RPS_Game = rps.rock_paper_scissors(window, images)
        elif type == 2:
            TTT_game = ttt.tic_tac_toe(window, images)
def on_close():
    window.destroy()
if __name__ == '__main__':
    window = tk.Tk()
    window.title('Mini Games')
    window.config(bg='#6F61C0')
    window.geometry('450x600')
    window.resizable(False, False)
    images = resized_images()
    window.iconphoto(True, images['mg_icon'])
    Title_label = tk.Label(window, image=images['Title'], bg='#6F61C0')
    Title_label.pack(pady=20)
    button_frame = tk.Frame(window, bg='#6F61C0', width=180, height=300)
    button_frame.pack(pady=30)
    RPS_button = tk.Button(
        button_frame, image=images['RPS'], bg='#6F61C0', borderwidth=0, activebackground='#6F61C0', command= lambda: Game_start(1))
    RPS_button.grid(row=0, column=0, pady=5)
    TTT_button = tk.Button(
        button_frame, image=images['TTT'], bg='#6F61C0', borderwidth=0, activebackground='#6F61C0', command= lambda: Game_start(2))
    TTT_button.grid(row=1, column=0, pady=5)
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()