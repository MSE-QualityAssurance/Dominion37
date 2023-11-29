import random

class Deck:
    def __init__(self):
        self.cards = []
        self.discard_pile = []

    def draw(self):
        # Draw a single card from the deck
        if len(self.cards) > 0:
            return self.cards.pop(0)
        return None

    def reshuffle_from_discard(self, discard_pile):
        # Add discard pile to deck and shuffle
        self.cards.extend(discard_pile)
        random.shuffle(self.cards)
        discard_pile.clear()

    def shuffle(self):
        # Shuffle the deck
        random.shuffle(self.cards)
