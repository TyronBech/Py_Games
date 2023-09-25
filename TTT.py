import tkinter as tk # Importing tkinter for the window
import random # Importing random to give random choices to computer and to identify who's going to play first
import Game_class as gc # Importing the parent class to get necessary methods and constructor

# Tic-Tac-Toe class
class tic_tac_toe(gc.Game_Setup):
    # Constructor of the class
    def __init__(self, main_window, images):
        # Icon of the Tic-Tac-Toe window
        icon = images['TTT_icon']
        # Calling the parent class constructor to build the window
        super().__init__(main_window, images, icon)
        self.TTT_title = tk.Label(
            self.class_window, image=self.images['TTT_title'], bg=self.CONFIGS['c1'])
        self.TTT_title.pack()
        self.create_board()
    # This method is going to create a board to play
    def create_board(self):
        self.positions = [-1] * 9
        self.turn = random.choice([1, 2])
        self.board_buttons()
        self.class_window.update()
        if self.turn == 1:
            self.Computer()
    # This method is responsible for creating buttons
    # for the game
    def board_buttons(self):
        # Frame to store all the buttons
        self.TTT_frame = tk.Frame(
            self.class_window, bg=self.CONFIGS['c1'], width=399, height=399)
        self.TTT_frame.pack()
        # Array of buttons is stored to button_list variable
        self.buttons_list = list()
        # loop to create buttons one by one
        for i in range(9):
            button = tk.Button(
                self.TTT_frame, image=self.images['blank_b'], bg=self.CONFIGS['c1'], borderwidth=0, activebackground=self.CONFIGS['c1'],
                command=lambda idx=i: self.Player(idx)
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons_list.append(button)
    # This method is responsible to create a random choice for the computer
    def Computer(self):
        while True:
            computer_choice = random.randint(0, 8)
            if self.positions[computer_choice] == -1:
                self.positions[computer_choice] = 0  # Computer's move (O)
                self.buttons_list[computer_choice].config(
                    image=self.images['o_b'], state=tk.DISABLED)
                for i in range(9):
                    if self.positions[i] == -1:
                        self.buttons_list[i].config(state=tk.NORMAL)
                self._identify_winner()
                break
    # This medthod is used bt the buttons as command to get the user choice
    def Player(self, index):
        if self.positions[index] == -1:
            self.positions[index] = 1
            self.buttons_list[index].config(
                image=self.images['x_b'], state=tk.DISABLED)
            for button in self.buttons_list:
                button.config(state=tk.DISABLED)
            if not self._identify_winner():
                self.class_window.after(1700, self.Computer)
    # This method will identify the combinations of the game
    # if the board is full and there's no combination
    # it will disabled the buttons and calling a draw
    def _identify_winner(self):
        # Possible combinations
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            a, b, c = combo
            if self.positions[a] == self.positions[b] == self.positions[c] != -1:
                winner = self.positions[a]
                self.Display_winner_Draw(winner)
                self.close_button(winner, a, b, c)
                return True
        # Checking if the board if full
        if all(pos != -1 for pos in self.positions):
            self.Display_winner_Draw(-1)
            self.close_button(-1, -1, -1, -1)
            return True
        return False
    # This method will display who's winner of the match else it will display draw
    def Display_winner_Draw(self, player):
        if player == 1:
            winner_label = tk.Label(self.TTT_frame, text='You Win!!!',
                                    font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
        elif player == 0:
            winner_label = tk.Label(self.TTT_frame, text='You Lose...',
                                    font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
        else:
            winner_label = tk.Label(self.TTT_frame, text='It\'s a Draw.',
                                    font=self.CONFIGS['font'], fg=self.CONFIGS['c3'], bg=self.CONFIGS['c1'])
        winner_label.grid(row=3, column=1)
        # Creating the 'try_again' and 'exit' buttons for the user
        try_again_button = tk.Button(
            self.TTT_frame, image=self.images['Try_again'], borderwidth=0, bg=self.CONFIGS['c1'], activebackground=self.CONFIGS['c1'], command=self._Restart)
        try_again_button.grid(row=3, column=0)
        exit_button = tk.Button(
            self.TTT_frame, image=self.images['Exit'], borderwidth=0, bg=self.CONFIGS['c1'], activebackground=self.CONFIGS['c1'], command=self._Exit_game)
        exit_button.grid(row=3, column=2)
    # This method will disable all the button once combination is created or if the match is draw
    def close_button(self, player, g1, g2, g3):
        # Conditional statement for draw
        if player == -1:
            for i in range(9):
                if self.positions[i] == -1:
                    self.buttons_list[i].config(
                        image=self.images['red_blank'], state=tk.DISABLED)
                elif self.positions[i] == 0:
                    self.buttons_list[i].config(
                        image=self.images['red_o_b'], state=tk.DISABLED)
                else:
                    self.buttons_list[i].config(
                        image=self.images['red_x_b'], state=tk.DISABLED)
        # Conditional statement for the computer
        elif player == 0:
            self.buttons_list[g1].config(
                image=self.images['green_o_b'], state=tk.DISABLED)
            self.buttons_list[g2].config(
                image=self.images['green_o_b'], state=tk.DISABLED)
            self.buttons_list[g3].config(
                image=self.images['green_o_b'], state=tk.DISABLED)
            for i in range(9):
                if self.positions[i] == 1:
                    self.buttons_list[i].config(
                        image=self.images['red_x_b'], state=tk.DISABLED)
                elif self.positions[i] == -1:
                    self.buttons_list[i].config(
                        image=self.images['red_blank'], state=tk.DISABLED)
                elif i != g1 and i != g2 and i != g3 and self.positions[i] == 0:
                    self.buttons_list[i].config(
                        image=self.images['red_o_b'], state=tk.DISABLED)
        # Conditional statement for the user
        else:
            self.buttons_list[g1].config(
                image=self.images['green_x_b'], state=tk.DISABLED)
            self.buttons_list[g2].config(
                image=self.images['green_x_b'], state=tk.DISABLED)
            self.buttons_list[g3].config(
                image=self.images['green_x_b'], state=tk.DISABLED)
            for i in range(9):
                if self.positions[i] == 0:
                    self.buttons_list[i].config(
                        image=self.images['red_o_b'], state=tk.DISABLED)
                elif self.positions[i] == -1:
                    self.buttons_list[i].config(
                        image=self.images['red_blank'], state=tk.DISABLED)
                elif i != g1 and i != g2 and i != g3 and self.positions[i] == 1:
                    self.buttons_list[i].config(
                        image=self.images['red_x_b'], state=tk.DISABLED)
    # This method will destroy and recreate a new blank board for next match
    def _Restart(self):
        self.TTT_frame.destroy()
        self.create_board()
