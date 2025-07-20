import tkinter as tk
from tkinter import simpledialog, messagebox
from OreskossTCG.models import Deck, Card
from OreskossTCG.storage import save_decks, load_decks

class OreskossTCGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.decks = load_decks()
        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Flashcard App", font=("Arial", 24)).pack(pady=10)
        tk.Button(self.root, text="Add Deck", width=20, command=self.add_deck).pack(pady=5)
        tk.Button(self.root, text="Play Deck", width=20, command=self.choose_deck_to_play).pack(pady=5)

    def add_deck(self):
        name = simpledialog.askstring("Deck Name", "Enter deck name:")
        if name:
            new_deck = Deck(name)
            self.decks.append(new_deck)
            self.add_card_to_deck(new_deck)
            save_decks(self.decks)

    def add_card_to_deck(self, deck):
        while True:
            front = simpledialog.askstring("Add Card", "Front text (Cancel to stop):")
            if not front:
                break
            back = simpledialog.askstring("Add Card", "Back text:")
            if back:
                deck.cards.append(Card(front, back))
        save_decks(self.decks)

    def choose_deck_to_play(self):
        if not self.decks:
            messagebox.showinfo("No decks", "Please create a deck first.")
            return
        for widget in self.root.winfo_children():
            widget.destroy()
        for deck in self.decks:
            tk.Button(self.root, text=deck.name, width=30,
                      command=lambda d=deck: self.play_deck(d)).pack(pady=2)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def play_deck(self, deck):
        self.index = 0
        self.current_deck = deck
        self.show_card()

    def show_card(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.index >= len(self.current_deck.cards):
            messagebox.showinfo("End", "You've reviewed all cards.")
            self.main_menu()
            return

        card = self.current_deck.cards[self.index]
        label = tk.Label(self.root, text=card.front, font=("Arial", 20))
        label.pack(pady=20)

        def flip():
            label.config(text=card.back)
            next_button.config(text="Next", command=self.next_card)

        next_button = tk.Button(self.root, text="Show Answer", command=flip)
        next_button.pack()

    def next_card(self):
        self.index += 1
        self.show_card()
