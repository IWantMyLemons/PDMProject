import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
import urllib.request
import io


def init_search_tab(self):
    ttk.Label(self.search_tab, text="Card Name").grid(row=0, column=0)
    self.search_entry = ttk.Entry(self.search_tab, width=30)
    self.search_entry.grid(row=0, column=1)
    ttk.Button(self.search_tab, text="Search",
               command=lambda: search_card(self)).grid(row=0, column=2)

    self.search_result = tk.Text(self.search_tab, height=10, width=60)
    self.search_result.grid(row=1, column=0, columnspan=3, pady=10)

    self.art_label = ttk.Label(self.search_tab)
    self.art_label.grid(row=2, column=0, columnspan=3)


def search_card(self):
    card_name = self.search_entry.get()
    res = self.controller.get_card_by_name(card_name)
    self.search_result.delete(1.0, tk.END)
    if res.is_success:
        card = res.payload
        self.search_result.insert(tk.END, f"Name: {card.card_name}\n")
        self.search_result.insert(tk.END, f"Description: {
            card.card_description}\n")
        self.search_result.insert(tk.END, f"Distributor: {
            card.distributor_name}\n")
        load_image(self, card.card_art)
    else:
        self.search_result.insert(tk.END, res.message)
        self.art_label.config(image='')


def load_image(self, url):
    try:
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        im = Image.open(io.BytesIO(raw_data))
        im.thumbnail((200, 200))
        self.img = ImageTk.PhotoImage(im)
        self.art_label.config(image=self.img)
    except Exception as e:
        print("Error loading image:", e)
        self.art_label.config(text="[Image Load Failed]")
