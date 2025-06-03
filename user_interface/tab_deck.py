from tkinter import ttk


def init_deck_tab(self):
    ttk.Label(self.deck_tab, text="Card Name").grid(row=0, column=0)
    self.deck_card_entry = ttk.Entry(self.deck_tab, width=30)
    self.deck_card_entry.grid(row=0, column=1)

    ttk.Label(self.deck_tab, text="Deck Name").grid(row=1, column=0)
    self.deck_id_entry = ttk.Entry(self.deck_tab, width=30)
    self.deck_id_entry.grid(row=1, column=1)

    self.deck_res_label = ttk.Label(self.deck_tab, text="")
    self.deck_res_label.grid(row=3, column=0)
    ttk.Button(self.deck_tab, text="Add to Deck",
               command=lambda: add_card_to_deck(self)).grid(row=2, column=1)


def add_card_to_deck(self):
    card = self.deck_card_entry.get()
    deck = self.deck_id_entry.get()
    res = self.controller.add_card_to_deck(card, deck)
    self.deck_res_label.config(text=res.message)
