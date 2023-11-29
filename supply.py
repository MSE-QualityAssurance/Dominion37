class Supply:
    def __init__(self, card_sets):
        # card_sets is a dictionary with card names as keys and tuples (card object, count) as values
        self.available_cards = card_sets  

    def buy(self, card_name):
        # Method to buy a card from the supply
        if card_name in self.available_cards and self.available_cards[card_name][1] > 0:
            self.available_cards[card_name] = (self.available_cards[card_name][0], self.available_cards[card_name][1] - 1)
            return self.available_cards[card_name][0]
        else:
            return None  # Card not available or out of stock
