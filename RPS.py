import tkinter as tk # Importing the tkinter for the window
import random # Importing random to get random choice for the computer
import Game_class as gc # Importing the parent class to get necessary methods and constructor

# Rock-Paper-Scissors class
class rock_paper_scissors(gc.Game_Setup):
    # Constructor of the class
    def __init__(self, main_window, images):
        # Icon of the Rock-Paper_scissors game
        icon = images['RPS_icon']
        # Calling the parent class constructor to build the window
        super().__init__(main_window, images, icon)
        self.RPS_title = tk.Label(
            self.class_window, image=self.images['RPS_title'], bg=self.CONFIGS['c1'])
        self.RPS_title.pack(pady=30)
        self.RPS_Buttons()
    # This medthod is responsible for creating button for the user
    def RPS_Buttons(self):
        self.frame = tk.Frame(
            self.class_window, bg=self.CONFIGS['c1'], width=180, height=300)
        self.frame.pack(padx=10, pady=10, side=tk.LEFT)
        self.rock_button = tk.Button(
            self.frame, image=self.images['Rock'], borderwidth=0, bg=self.CONFIGS['c1'], activebackground=self.CONFIGS['c1'], command=lambda: self._Gameplay('Rock'))
        self.rock_button.grid(row=0, column=0, pady=5)
        self.paper_button = tk.Button(
            self.frame, image=self.images['Paper'], borderwidth=0, bg=self.CONFIGS['c1'], activebackground=self.CONFIGS['c1'], command=lambda: self._Gameplay('Paper'))
        self.paper_button.grid(row=1, column=0, pady=5)
        self.scissors_button = tk.Button(
            self.frame, image=self.images['Scissors'], borderwidth=0, bg=self.CONFIGS['c1'], activebackground=self.CONFIGS['c1'], command=lambda: self._Gameplay('Scissors'))
        self.scissors_button.grid(row=2, column=0, pady=5)
        self.exit_button = tk.Button(
            self.frame, image=self.images['Exit'], borderwidth=0, bg=self.CONFIGS['c1'], activebackground=self.CONFIGS['c1'], command=self._Exit_game)
        self.exit_button.grid(row=3, column=0, pady=5)
        self.class_window.update()
    # This medthod is calld to disable the button and show the choices
    def _Gameplay(self, user_choice):
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)
        self.exit_button.config(state=tk.DISABLED)
        self.gameplayFrame = tk.Frame(self.class_window, bg=self.CONFIGS['c1'])
        self.gameplayFrame.place(x=180, y=330)
        if user_choice == 'Rock':
            user_label = tk.Label(
                self.gameplayFrame, image=self.images['Rock_hand'], bg=self.CONFIGS['c1'])
            text_label = tk.Label(self.gameplayFrame, text='Rock',
                                    font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
        elif user_choice == 'Paper':
            user_label = tk.Label(
                self.gameplayFrame, image=self.images['Paper_hand'], bg=self.CONFIGS['c1'])
            text_label = tk.Label(self.gameplayFrame, text='Paper',
                                    font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
        elif user_choice == 'Scissors':
            user_label = tk.Label(
                self.gameplayFrame, image=self.images['Scissors_hand'], bg=self.CONFIGS['c1'])
            text_label = tk.Label(self.gameplayFrame, text='Scissors',
                                    font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
        user_label.grid(row=0, column=0, padx=3, pady=3)
        text_label.grid(row=1, column=0, pady=2)
        vs_label = tk.Label(self.gameplayFrame,
                            image=self.images['vs'], bg=self.CONFIGS['c1'])
        vs_label.grid(row=0, column=1, padx=3, pady=3, rowspan=2)
        self.class_window.update()
        self.class_window.after(2000, lambda: self.Computer(user_choice))
    # This method is used to get a random choice for the computer
    def Computer(self, user_choice):
        # Dictionary of choices for the computer
        computer_choices = {
            'Rock': 'Rock_computer',
            'Paper': 'Paper_computer',
            'Scissors': 'Scissors_computer'
        }
        # Random result for the computer
        generated_key, generated_value = random.choice(
            list(computer_choices.items()))
        computer_label = tk.Label(
            self.gameplayFrame, image=self.images[generated_value], bg=self.CONFIGS['c1'])
        computer_label.grid(row=0, column=2, padx=3, pady=3)
        computer_text_label = tk.Label(self.gameplayFrame, text=generated_key,
                                        font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
        computer_text_label.grid(row=1, column=2, pady=2)
        self.class_window.after(
            2000, lambda x=user_choice, y=generated_key: self._identify_winner(x, y))
    # This method is going to identify who won the match and display necessary labels and buttons
    def _identify_winner(self, user, computer):
        if user == 'Rock':
            if computer == 'Rock':
                show_winner = tk.Label(self.gameplayFrame, text='It is a tie.',
                                        font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
            elif computer == 'Paper':
                show_winner = tk.Label(self.gameplayFrame, text='You lose.',
                                        font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
            else:
                show_winner = tk.Label(self.gameplayFrame, text='You win!',
                                        font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
        elif user == 'Paper':
            if computer == 'Rock':
                show_winner = tk.Label(self.gameplayFrame, text='You win!',
                                        font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
            elif computer == 'Paper':
                show_winner = tk.Label(self.gameplayFrame, text='It is a tie.',
                                        font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
            else:
                show_winner = tk.Label(self.gameplayFrame, text='You lose.',
                                        font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
        else:
            if computer == 'Rock':
                show_winner = tk.Label(self.gameplayFrame, text='You lose.',
                                        font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
            elif computer == 'Paper':
                show_winner = tk.Label(self.gameplayFrame, text='You win!',
                                        font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
            else:
                show_winner = tk.Label(self.gameplayFrame, text='It is a tie.',
                                        font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
        show_winner.grid(row=2, column=0, columnspan=3)
        self.try_again_button = tk.Button(
            self.gameplayFrame, image=self.images['Try_again'], borderwidth=0, bg=self.CONFIGS['c1'], activebackground=self.CONFIGS['c1'], command=self._Restart)
        self.try_again_button.grid(row=3, column=0, columnspan=3, pady=10)
    # This method is used to restart the game by destroying the frame and enabling the buttons back
    def _Restart(self):
        self.gameplayFrame.destroy()
        self.try_again_button.destroy()
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)
        self.exit_button.config(state=tk.NORMAL)