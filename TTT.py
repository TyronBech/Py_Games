import tkinter as tk
import main as mn
import random

class tic_tac_toe(object):
    def __init__(self, main_window, images):
        self.main_window = main_window
        self.images = images
        self.class_window = tk.Toplevel()
        self.class_window.config(bg=mn.COLORS[1])
        self.class_window.geometry('450x600')
        self.class_window.resizable(False, False)
        self.class_window.protocol('WM_DELETE_WINDOW', lambda: self._on_close(main_window))
        self.TTT_title = tk.Label(self.class_window, image=self.images['TTT_title'], bg=mn.COLORS[1])
        self.TTT_title.pack()
        self.create_board()
    def create_board(self):
        self.positions = [-1] * 9
        self.turn = random.choice([1, 2])
        self.board_buttons()
        self.class_window.update()
        if self.turn == 1:
            self.Computer()
    def board_buttons(self):
        self.TTT_frame = tk.Frame(self.class_window, bg=mn.COLORS[1], width=399, height=399)
        self.TTT_frame.pack()
        self.buttons_list = list()
        for i in range(9):
            button = tk.Button(
                self.TTT_frame, image=self.images['blank_b'], bg=mn.COLORS[1], borderwidth=0, activebackground=mn.COLORS[1],
                command=lambda idx=i: self.Player(idx)
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons_list.append(button)
    def Computer(self):
        while True:
            computer_choice = random.randint(0, 8)
            if self.positions[computer_choice] == -1:
                self.positions[computer_choice] = 0  # Computer's move (O)
                self.buttons_list[computer_choice].config(image=self.images['o_b'], state=tk.DISABLED)
                for i in range(9):
                    if self.positions[i] == -1:
                        self.buttons_list[i].config(state=tk.NORMAL)
                self.check_winner()
                break
    def Player(self, index):
        if self.positions[index] == -1:
            self.positions[index] = 1
            self.buttons_list[index].config(image=self.images['x_b'], state=tk.DISABLED)
            for button in self.buttons_list:
                button.config(state=tk.DISABLED)
            if not self.check_winner():
                self.class_window.after(1700, self.Computer)
    def check_winner(self):
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
        if all(pos != -1 for pos in self.positions):
            self.Display_winner_Draw(-1)
            self.close_button(-1, -1, -1, -1)
            return True
        return False
    def Display_winner_Draw(self, player):
        if player == 1:
            winner_label = tk.Label(self.TTT_frame, text='You Win!!!', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
        elif player == 0:
            winner_label = tk.Label(self.TTT_frame, text='You Lose...', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
        else:
            winner_label = tk.Label(self.TTT_frame, text='It\'s a Draw.', font=('Consolas', 14, 'bold'), fg=mn.COLORS[3], bg=mn.COLORS[1])
        winner_label.grid(row=3, column=1)
        try_again_button = tk.Button(
            self.TTT_frame, image=self.images['Try_again'], borderwidth=0, bg=mn.COLORS[1], activebackground=mn.COLORS[1], command=self._Restart)
        try_again_button.grid(row=3, column=0)
        exit_button = tk.Button(
            self.TTT_frame, image=self.images['Exit'], borderwidth=0, bg=mn.COLORS[1], activebackground=mn.COLORS[1], command=self._Exit_game)
        exit_button.grid(row=3, column=2)
    def close_button(self, player, g1, g2, g3):
        if player == -1:
            for i in range(9):
                if self.positions[i] == -1:
                    self.buttons_list[i].config(image=self.images['red_blank'], state=tk.DISABLED)
                elif self.positions[i] == 0:
                    self.buttons_list[i].config(image=self.images['red_o_b'], state=tk.DISABLED)
                else:
                    self.buttons_list[i].config(image=self.images['red_x_b'], state=tk.DISABLED)
        elif player == 0:
            self.buttons_list[g1].config(image=self.images['green_o_b'], state=tk.DISABLED)
            self.buttons_list[g2].config(image=self.images['green_o_b'], state=tk.DISABLED)
            self.buttons_list[g3].config(image=self.images['green_o_b'], state=tk.DISABLED)
            for i in range(9):
                if self.positions[i] == 1:
                    self.buttons_list[i].config(image=self.images['red_x_b'], state=tk.DISABLED)
                elif self.positions[i] == -1:
                    self.buttons_list[i].config(image=self.images['red_blank'], state=tk.DISABLED)
                elif i != g1 and i != g2 and i != g3 and self.positions[i] == 0:
                    self.buttons_list[i].config(image=self.images['red_o_b'], state=tk.DISABLED)
        else:
            self.buttons_list[g1].config(image=self.images['green_x_b'], state=tk.DISABLED)
            self.buttons_list[g2].config(image=self.images['green_x_b'], state=tk.DISABLED)
            self.buttons_list[g3].config(image=self.images['green_x_b'], state=tk.DISABLED)
            for i in range(9):
                if self.positions[i] == 0:
                    self.buttons_list[i].config(image=self.images['red_o_b'], state=tk.DISABLED)
                elif self.positions[i] == -1:
                    self.buttons_list[i].config(image=self.images['red_blank'], state=tk.DISABLED)
                elif i != g1 and i != g2 and i != g3 and self.positions[i] == 1:
                    self.buttons_list[i].config(image=self.images['red_x_b'], state=tk.DISABLED)
    def _Restart(self):
        self.TTT_frame.destroy()
        self.create_board()
    def _on_close(self, main_window):
        self.class_window.destroy()
        main_window.deiconify()
    def _Exit_game(self):
        self.class_window.destroy()
        self.main_window.deiconify()