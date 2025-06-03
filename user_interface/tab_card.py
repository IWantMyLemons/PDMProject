from tkinter import ttk


def init_card_tab(self):
    labels = ["Card Name", "Description", "Art URL", "Distributor"]
    self.card_entries = []

    for i, label in enumerate(labels):
        ttk.Label(self.card_tab, text=label).grid(
            row=i, column=0, sticky="e")
        entry = ttk.Entry(self.card_tab, width=40)
        entry.grid(row=i, column=1, pady=2)
        self.card_entries.append(entry)

    ttk.Button(self.card_tab, text="Save Card",
               command=lambda: save_card(self)).grid(row=len(labels), column=1)

    self.response_text = ttk.Label(self.card_tab, text="")
    self.response_text.grid(row=len(labels)+1, column=1)


def save_card(self):
    name, desc, art, dist = [e.get() for e in self.card_entries]
    res = self.controller.save_card(name, desc, art, dist)
    print(res.message)
    self.response_text.config(text=res.message)
