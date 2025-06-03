
import tkinter as tk
from tkinter import ttk


def init_view_tab(self):
    ttk.Label(self.view_tab, text="Deck Name").grid(row=0, column=0)
    self.view_deck_entry = ttk.Entry(self.view_tab, width=10)
    self.view_deck_entry.grid(row=0, column=1)

    self.card_listbox = tk.Listbox(self.view_tab, width=60)
    self.card_listbox.grid(row=1, column=0, columnspan=2, pady=5)

    ttk.Button(self.view_tab, text="List Cards",
               command=lambda: list_cards_in_deck(self)).grid(row=0, column=2)


def list_cards_in_deck(self):
    deck_name = self.view_deck_entry.get()
    res = self.controller.get_cards_by_deck(deck_name)
    self.card_listbox.delete(0, tk.END)

    if not res.is_success:
        self.card_listbox.insert(tk.END, res.message)
        return

    cards = res.payload
    for card in cards:
        self.card_listbox.insert(tk.END, card)
