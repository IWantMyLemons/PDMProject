from models.card import Card


class CardFactory:
    @staticmethod
    def new(
        card_name: str,
        card_description: str,
        card_art: str,
        distributor_name: str,
    ) -> Card:
        return Card(
            card_name=card_name,
            card_description=card_description,
            card_art=card_art,
            distributor_name=distributor_name,
        )
