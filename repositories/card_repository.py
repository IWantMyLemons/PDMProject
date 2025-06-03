import sqlite3
from factories.card_factory import CardFactory
from models.card import Card


class CardRepository:
    _instance = None  # singleton class-level attribute

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CardRepository, cls).__new__(cls)
        return cls._instance

    # Connect to database when created
    def __init__(self):
        self.con = sqlite3.connect("card_database.db")
        with open("schema.sql", "r") as schema:
            self.con.executescript(schema.read())

    # Connect to database when created
    def __del__(self):
        if hasattr(self, 'con'):
            self.con.close()

    # Gets a card by it's name
    def get_card(self, card_name: str) -> Card | None:
        cur = self.con.cursor()
        try:
            res = cur.execute("""
                SELECT cardName, cardDescription, cardArt, distributorName
                FROM card
                LEFT JOIN distributor
                    ON card.distributorID = distributor.distributorID
                WHERE cardName = ?
                """, (card_name,))
            row = res.fetchone()
            if row is None:
                return
            return CardFactory.new(*row)
        finally:
            cur.close()

    # Gets cards inside a deck by name
    def get_cards(self, deck_name: str) -> Card | None:
        cur = self.con.cursor()
        try:
            res = cur.execute("""
                SELECT cardName, cardDescription, cardArt, distributorName
                FROM deck
                LEFT JOIN cardDeckLink
                    ON deck.deckID = cardDeckLink.deckID
                LEFT JOIN card
                    ON card.cardID = cardDeckLink.cardID
                LEFT JOIN distributor
                    ON card.distributorID = distributor.distributorID
                WHERE deckName = ?
                """, (deck_name,))
            rows = res.fetchall()
            if rows is None:
                return
            return [CardFactory.new(*row) for row in rows]
        finally:
            cur.close()

    # Adds a new card
    def add_card(self, card: Card) -> bool:
        cur = self.con.cursor()
        try:
            distributor_id = cur.execute("""
                SELECT distributorID
                FROM distributor
                WHERE distributorName = ?
                """, (card.distributor_name,)).fetchone()
            if distributor_id is None:
                return False
            cur.execute("""
                INSERT INTO card (
                    cardName,
                    cardDescription,
                    cardArt,
                    distributorID
                ) VALUES (?, ?, ?, ?)
                """, (
                card.card_name,
                card.card_description,
                card.card_art,
                distributor_id[0],))
            self.con.commit()
            return True
        finally:
            cur.close()
        return False

    # adds a new card to a deck
    # creates a deck if one does not exist
    def add_card_to_deck(self, card_name: str, deck_name: str):
        cur = self.con.cursor()
        try:
            card_id = cur.execute("""
                SELECT cardID
                FROM card
                WHERE cardName = ?
                """, (card_name,)).fetchone()
            if card_id is None:
                return False

            deck_id = cur.execute("""
                SELECT deckID
                FROM deck
                WHERE deckName = ?
                """, (deck_name,)).fetchone()
            if deck_id is None:
                cur.execute("""
                    INSERT INTO deck (
                        deckName
                    ) VALUES (?)
                    """, (deck_name,))
                deck_id = cur.execute("""
                    SELECT deckID
                    FROM deck
                    WHERE deckName = ?
                    """, (deck_name,)).fetchone()
            cur.execute("""
                INSERT INTO cardDeckLink (
                    cardID,
                    deckID
                ) VALUES (?, ?)
                """, (card_id[0], deck_id[0],))
            self.con.commit()
            return True
        finally:
            cur.close()
        return False

    # Adds a new distributor
    def add_distributor(self, name: str) -> bool:
        cur = self.con.cursor()
        try:
            cur.execute("""
                INSERT INTO distributor (
                    distributorName
                ) VALUES (?)
                """, (name,))
            self.con.commit()
            return True
        finally:
            cur.close()
        return False
