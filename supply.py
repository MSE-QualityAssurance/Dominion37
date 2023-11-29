from card import *

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

    def setup_initial_supply(self):
        # Example setup for the supply
        # This should be modified based on the actual game setup you want
        from card import Copper, Silver, Gold, Estate, Duchy, Province, Smithy, Village
        self.available_cards = {
            "Copper": (Copper(), 60),  # Assuming 60 Copper cards
            "Silver": (Silver(), 40),  # Assuming 40 Silver cards
            "Gold": (Gold(), 30),      # Assuming 30 Gold cards
            "Estate": (Estate(), 24),  # Assuming 24 Estate cards
            "Duchy": (Duchy(), 12),    # Assuming 12 Duchy cards
            "Province": (Province(), 12), # Assuming 12 Province cards
            "Smithy": (Smithy(), 10),  # Assuming 10 Smithy cards
            "Village": (Village(), 10) # Assuming 10 Village cards
        }
