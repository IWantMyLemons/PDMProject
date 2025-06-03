from tkinter import ttk


def init_distributor_tab(self):
    ttk.Label(self.distributor_tab, text="Distributor Name").grid(
        row=0, column=0, sticky="e")
    entry = ttk.Entry(self.distributor_tab, width=40)
    entry.grid(row=0, column=1, pady=2)
    self.distributor_entry = entry

    ttk.Button(self.distributor_tab, text="Save Distributor",
               command=lambda: save_distributor(self)).grid(row=1, column=1)

    self.response_text = ttk.Label(self.distributor_tab, text="")
    self.response_text.grid(row=2, column=1)


def save_distributor(self):
    name = self.distributor_entry.get()
    res = self.controller.save_distributor(name)
    print(res.message)
    self.response_text.config(text=res.message)
