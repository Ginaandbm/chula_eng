import tkinter as tk
import random

# List of Thai consonants and their pronunciation
thai_consonants = [
    ("ก", "gor kai"), ("ข", "khor khai"), ("ฃ", "khor khuad"),
    ("ค", "khor khwai"), ("ฅ", "khor khon"), ("ฆ", "khor rakhang"),
    ("ง", "ngor ngu"), ("จ", "jor jan"), ("ฉ", "chor ching"),
    ("ช", "chor chang"), ("ซ", "sor so"), ("ฌ", "chor choe"),
    ("ญ", "yor ying"), ("ฎ", "dor cha-da"), ("ฏ", "tor pa-tak")
]


class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")

        self.current_index = random.randint(0, len(thai_consonants) - 1)
        self.is_flipped = False

        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief=tk.RAISED, bd=3)
        self.card_frame.pack(pady=20)

        self.card_label = tk.Label(self.card_frame, text=thai_consonants[self.current_index][0],
                                   font=("Arial", 50), bg="white")
        self.card_label.pack(expand=True)

        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(side=tk.LEFT, padx=20)

        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(side=tk.RIGHT, padx=20)

    def flip_card(self):
        if self.is_flipped:
            self.card_label.config(text=thai_consonants[self.current_index][0])
        else:
            self.card_label.config(text=thai_consonants[self.current_index][1])
        self.is_flipped = not self.is_flipped

    def next_card(self):
        self.current_index = random.randint(0, len(thai_consonants) - 1)
        self.is_flipped = False
        self.card_label.config(text=thai_consonants[self.current_index][0])


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardGame(root)
    root.mainloop()
