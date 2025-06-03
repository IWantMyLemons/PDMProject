class Card:
    def __init__(
        self,
        card_name: str,
        card_description: str,
        card_art: str,
        distributor_name: str,
    ):
        self.card_name = card_name
        self.card_description = card_description
        self.card_art = card_art
        self.distributor_name = distributor_name

    def __repr__(self):
        return f"Card(card_name={repr(self.card_name)},card_description={repr(self.card_description)},card_art={repr(self.card_art)},distributor_name={repr(self.distributor_name)}"
