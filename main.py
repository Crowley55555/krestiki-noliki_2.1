import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.root.geometry("400x500")

        self.current_player = "X"
        self.buttons = []
        self.player_scores = {"X": 0, "O": 0}
        self.wins_to_win = 3
        self.player_choice = None

        self.create_widgets()

    def create_widgets(self):
        self.score_label = tk.Label(self.root, text=f"Счет: X - {self.player_scores['X']} | O - {self.player_scores['O']}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(self.game_frame, text="", font=("Arial", 20), width=5, height=2,
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.root, text="Сбросить игру", font=("Arial", 14), command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.choose_player_dialog()

    def choose_player_dialog(self):
        self.player_choice = tk.StringVar(value="X")
        dialog = tk.Toplevel(self.root)
        dialog.title("Выбор игрока")
        dialog.geometry("200x150")

        label = tk.Label(dialog, text="Выберите, чем будете играть:", font=("Arial", 12))
        label.pack(pady=10)

        x_radio = tk.Radiobutton(dialog, text="X", variable=self.player_choice, value="X", font=("Arial", 12))
        x_radio.pack()

        o_radio = tk.Radiobutton(dialog, text="O", variable=self.player_choice, value="O", font=("Arial", 12))
        o_radio.pack()

        confirm_button = tk.Button(dialog, text="Подтвердить", font=("Arial", 12), command=lambda: self.start_game(dialog))
        confirm_button.pack(pady=10)

    def start_game(self, dialog):
        self.current_player = self.player_choice.get()
        dialog.destroy()

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] != "":
            return

        self.buttons[row][col]["text"] = self.current_player

        if self.check_winner():
            self.player_scores[self.current_player] += 1
            self.update_score_label()
            messagebox.showinfo("Игра завершена", f"Победил игрок {self.current_player}")
            if self.player_scores[self.current_player] >= self.wins_to_win:
                messagebox.showinfo("Поздравления", f"Игрок {self.current_player} выиграл {self.wins_to_win} раз!")
                self.reset_all()
            else:
                self.reset_game()
            return

        if self.check_draw():
            messagebox.showinfo("Игра завершена", "Ничья!")
            self.reset_game()
            return

        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True

        return False

    def check_draw(self):
        for row in self.buttons:
            for btn in row:
                if btn["text"] == "":
                    return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")

    def reset_all(self):
        self.player_scores = {"X": 0, "O": 0}
        self.update_score_label()
        self.reset_game()

    def update_score_label(self):
        self.score_label.config(text=f"Счет: X - {self.player_scores['X']} | O - {self.player_scores['O']}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()