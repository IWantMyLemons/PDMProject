from repositories.card_repository import CardRepository
from factories.card_factory import CardFactory
from models.response import Response


class CardController:
    def __init__(self):
        self.repo = CardRepository()

    def get_card_by_name(self, name: str) -> Response:
        name = name.lower()
        card = self.repo.get_card(name)
        if card is None:
            return Response(False, "Card not found :/")
        return Response(True, "Found card :3", card)

    def save_card(self, name, desc, art, dist) -> Response:
        name = name.lower()
        desc = desc.lower()
        art = art.lower()
        dist = dist.lower()
        if len(name) <= 0:
            return Response(False, "Name must not be empty")
        if len(desc) <= 0:
            return Response(False, "Description must not be empty")
        if len(art) <= 0:
            return Response(False, "Art must not be empty")
        if len(dist) <= 0:
            return Response(False, "Distributor must not be empty")
        res = self.repo.add_card(CardFactory.new(name, desc, art, dist))
        if not res:
            return Response(False, "Failed to save card (does your distributor exist?)")
        return Response(True, "Saved card :D")

    def save_distributor(self, name) -> Response:
        name = name.lower()
        if len(name) <= 0:
            return Response(False, "Name must not be empty")
        res = self.repo.add_distributor(name)
        if not res:
            return Response(False, "Failed to create distributor (does your distributor already exist?)")
        return Response(True, "Created distributor :D")

    def get_cards_by_deck(self, deck_name: str) -> Response:
        deck_name = deck_name.lower()
        cards = self.repo.get_cards(deck_name)
        if len(cards) == 0:
            return Response(False, "Deck not found :/")
        return Response(True, "Found deck :3", cards)

    def add_card_to_deck(self, card_name: str, deck_name: str):
        card_name = card_name.lower()
        deck_name = deck_name.lower()
        res = self.repo.add_card_to_deck(card_name, deck_name)
        if not res:
            return Response(False, "Failed to add card (does your card exist?)")
        return Response(True, "Added card :D")
