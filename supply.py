class Supply:
    def __init__(self, card_sets):
        self.available_cards = card_sets  # Dictionary of card types and their counts

    def buy(self, card_name):
        # Method to buy a card from the supply
