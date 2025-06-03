from tkinter import ttk

from controllers.card_controller import CardController

from user_interface import tab_card
from user_interface import tab_deck
from user_interface import tab_list
from user_interface import tab_search
from user_interface import tab_distributor


class CardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RuinaCardLibrary")
        self.controller = CardController()

        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill='both')

        self.card_tab = ttk.Frame(notebook)
        self.deck_tab = ttk.Frame(notebook)
        self.view_tab = ttk.Frame(notebook)
        self.search_tab = ttk.Frame(notebook)
        self.distributor_tab = ttk.Frame(notebook)

        notebook.add(self.card_tab, text='Add New Card')
        notebook.add(self.deck_tab, text='Add Card to Deck')
        notebook.add(self.view_tab, text='View Deck')
        notebook.add(self.search_tab, text='Search Card')
        notebook.add(self.distributor_tab, text='Add New Distributor')

        tab_card.init_card_tab(self)
        tab_deck.init_deck_tab(self)
        tab_list.init_view_tab(self)
        tab_search.init_search_tab(self)
        tab_distributor.init_distributor_tab(self)
