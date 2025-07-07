import tkinter as tk
from tkinter import messagebox
import random

class SnakeWaterGunGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍💧🔫 Snake Water Gun Game")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a2e')

        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.player_choice = None
        self.computer_choice = None

        self.choices = {
            'snake': {'emoji': '🐍', 'name': 'Snake', 'color': '#2ecc71'},
            'water': {'emoji': '💧', 'name': 'Water', 'color': '#3498db'},
            'gun': {'emoji': '🔫', 'name': 'Gun', 'color': '#e74c3c'}
        }

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, bg='#1a1a2e')
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(self.main_frame, text="🐍💧🔫 SNAKE WATER GUN",
                 font=('Arial', 28, 'bold'), bg='#1a1a2e', fg='white').pack(pady=20)

        self.player_score_label = tk.Label(self.main_frame, text="👤 Player: 0",
                                           font=('Arial', 18), bg='#1a1a2e', fg='#2ecc71')
        self.player_score_label.pack()
        self.computer_score_label = tk.Label(self.main_frame, text="🤖 Computer: 0",
                                             font=('Arial', 18), bg='#1a1a2e', fg='#e74c3c')
        self.computer_score_label.pack(pady=10)

        self.player_choice_label = tk.Label(self.main_frame, text="❓",
                                            font=('Arial', 60), bg='#1a1a2e', fg='white')
        self.player_choice_label.pack(pady=10)

        self.computer_choice_label = tk.Label(self.main_frame, text="❓",
                                              font=('Arial', 60), bg='#1a1a2e', fg='white')
        self.computer_choice_label.pack(pady=10)

        self.result_label = tk.Label(self.main_frame, text="",
                                     font=('Arial', 20), bg='#1a1a2e', fg='white')
        self.result_label.pack(pady=20)

        self.button_frame = tk.Frame(self.main_frame, bg='#1a1a2e')
        self.button_frame.pack(pady=30)

        for key, val in self.choices.items():
            btn = tk.Button(self.button_frame, text=f"{val['emoji']} {val['name']}",
                            font=('Arial', 16), bg=val['color'], fg='white',
                            padx=30, pady=15, command=lambda c=key: self.make_choice(c))
            btn.pack(side=tk.LEFT, padx=15)

        self.quit_btn = tk.Button(self.main_frame, text="❌ Quit Game",
                                  font=('Arial', 14), bg='#e74c3c', fg='white',
                                  command=self.root.destroy)
        self.quit_btn.pack(pady=10)

    def make_choice(self, choice):
        self.player_choice = choice
        self.computer_choice = random.choice(list(self.choices.keys()))

        self.player_choice_label.config(text=self.choices[self.player_choice]['emoji'])
        self.computer_choice_label.config(text=self.choices[self.computer_choice]['emoji'])

        result = self.get_result()

        if result == 'player':
            self.player_score += 1
            self.result_label.config(text="🎉 You win this round!", fg='#2ecc71')
        elif result == 'computer':
            self.computer_score += 1
            self.result_label.config(text="❌ Computer wins this round!", fg='#e74c3c')
        else:
            self.result_label.config(text="🤝 It's a tie!", fg='#f39c12')

        self.update_scores()

    def get_result(self):
        if self.player_choice == self.computer_choice:
            return 'tie'
        wins = {
            ('snake', 'water'),
            ('water', 'gun'),
            ('gun', 'snake')
        }
        if (self.player_choice, self.computer_choice) in wins:
            return 'player'
        return 'computer'

    def update_scores(self):
        self.player_score_label.config(text=f"👤 Player: {self.player_score}")
        self.computer_score_label.config(text=f"🤖 Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeWaterGunGame(root)
    root.mainloop()
