import tkinter as tk
from tkinter import messagebox
import main as mn
import random, time
class rock_paper_scissors(object):
    def __init__(self, main_window, images):
        self.images = images
        self.class_window = tk.Toplevel()
        self.class_window.config(bg=mn.COLORS[1])
        self.class_window.geometry('450x600')
        self.class_window.resizable(False, False)
        self.class_window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(main_window))
        self.RPS_title = tk.Label(self.class_window, image=self.images['RPS_title'], bg=mn.COLORS[1])
        self.RPS_title.pack(pady=30)
        self.frame = tk.Frame(self.class_window, bg=mn.COLORS[1], width=180, height=300)
        self.frame.pack(padx= 10, pady=10, side='left')
        self.rock_button = tk.Button(
            self.frame, image=self.images['Rock'], borderwidth=0, bg=mn.COLORS[1], activebackground=mn.COLORS[1], command= lambda: self.Gameplay('Rock'))
        self.rock_button.grid(row=0, column=0, pady=5)
        self.paper_button = tk.Button(
            self.frame, image=self.images['Paper'], borderwidth=0, bg=mn.COLORS[1], activebackground=mn.COLORS[1], command= lambda: self.Gameplay('Paper'))
        self.paper_button.grid(row=1, column=0, pady=5)
        self.scissors_button = tk.Button(
            self.frame, image=self.images['Scissors'], borderwidth=0, bg=mn.COLORS[1], activebackground=mn.COLORS[1], command= lambda: self.Gameplay('Scissors'))
        self.scissors_button.grid(row=2, column=0, pady=5)
        self.exit_button = tk.Button(
            self.frame, image=self.images['Exit'], borderwidth=0, bg=mn.COLORS[1], activebackground=mn.COLORS[1], command=lambda: self.Exit_game(main_window))
        self.exit_button.grid(row=3, column=0, pady=5)
        self.class_window.update()
    def Gameplay(self, user_choice):
        computer_choices = {
            'Rock' : 'Rock_computer',
            'Paper' : 'Paper_computer',
            'Scissors' : 'Scissors_computer'
        }
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)
        self.exit_button.config(state=tk.DISABLED)
        self.gameplayFrame = tk.Frame(self.class_window, bg=mn.COLORS[1])
        self.gameplayFrame.place(x=180, y=330)
        if user_choice == 'Rock':
            user_label = tk.Label(self.gameplayFrame, image=self.images['Rock_hand'], bg=mn.COLORS[1])
            user_label.grid(row=0, column=0, padx=3, pady=3)
            text_label = tk.Label(self.gameplayFrame, text='Rock', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
            text_label.grid(row=1, column=0, pady=2)
        elif user_choice == 'Paper':
            user_label = tk.Label(self.gameplayFrame, image=self.images['Paper_hand'], bg=mn.COLORS[1])
            user_label.grid(row=0, column=0, padx=3, pady=3)
            text_label = tk.Label(self.gameplayFrame, text='Paper', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
            text_label.grid(row=1, column=0, pady=2)
        elif user_choice == 'Scissors':
            user_label = tk.Label(self.gameplayFrame, image=self.images['Scissors_hand'], bg=mn.COLORS[1])
            user_label.grid(row=0, column=0, padx=3, pady=3)
            text_label = tk.Label(self.gameplayFrame, text='Scissors', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
            text_label.grid(row=1, column=0, pady=2)
        vs_label = tk.Label(self.gameplayFrame, image=self.images['vs'], bg=mn.COLORS[1])
        vs_label.grid(row=0, column=1, padx=3, pady=3, rowspan=2)
        self.class_window.update()
        generated_key, generated_value = random.choice(list(computer_choices.items()))
        time.sleep(2)
        computer_label = tk.Label(self.gameplayFrame, image=self.images[generated_value], bg=mn.COLORS[1])
        computer_label.grid(row=0, column=2, padx=3, pady=3)
        computer_text_label = tk.Label(self.gameplayFrame, text=generated_key, font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
        computer_text_label.grid(row=1, column=2, pady=2)
        self.class_window.update()
        time.sleep(2)
        self.identify_winner(user_choice, generated_key)
        self.try_again_button = tk.Button(
            self.gameplayFrame, image=self.images['Try_again'], borderwidth=0, bg=mn.COLORS[1], activebackground=mn.COLORS[1], command=self.Restart)
        self.try_again_button.grid(row=3, column=0, columnspan=3, pady=10)
    def identify_winner(self, user, computer):
        if user == 'Rock':
            if computer == 'Rock':
                show_winner = tk.Label(self.gameplayFrame, text='It is a tie.', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
                show_winner.grid(row=2, column=0, columnspan=3)
            elif computer == 'Paper':
                show_winner = tk.Label(self.gameplayFrame, text='You lose.', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
                show_winner.grid(row=2, column=0, columnspan=3)
            else:
                show_winner = tk.Label(self.gameplayFrame, text='You win!', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
                show_winner.grid(row=2, column=0, columnspan=3)
        elif user == 'Paper':
            if computer == 'Rock':
                show_winner = tk.Label(self.gameplayFrame, text='You win!', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
                show_winner.grid(row=2, column=0, columnspan=3)
            elif computer == 'Paper':
                show_winner = tk.Label(self.gameplayFrame, text='It is a tie.', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
                show_winner.grid(row=2, column=0, columnspan=3)
            else:
                show_winner = tk.Label(self.gameplayFrame, text='You lose.', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
                show_winner.grid(row=2, column=0, columnspan=3)
        else:
            if computer == 'Rock':
                show_winner = tk.Label(self.gameplayFrame, text='You lose.', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
                show_winner.grid(row=2, column=0, columnspan=3)
            elif computer == 'Paper':
                show_winner = tk.Label(self.gameplayFrame, text='You win!', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
                show_winner.grid(row=2, column=0, columnspan=3)
            else:
                show_winner = tk.Label(self.gameplayFrame, text='It is a tie.', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
                show_winner.grid(row=2, column=0, columnspan=3)
    def Restart(self):
        self.gameplayFrame.destroy()
        self.try_again_button.destroy()
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)
        self.exit_button.config(state=tk.NORMAL)
    def on_close(self, main_window):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.class_window.destroy()
            main_window.destroy()
    def Exit_game(self, main_window):
        self.class_window.destroy()
        main_window.deiconify()