from deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.hand = []
        self.discard_pile = []

    def draw_hand(self, num_cards=5):
        # Draw cards from the deck
        for _ in range(num_cards):
            if len(self.deck.cards) == 0:
                self.deck.reshuffle_from_discard(self.discard_pile)
            card = self.deck.draw()
            if card:
                self.hand.append(card)

    def play_card(self, card):
        # Play a card from hand
        if card in self.hand:
            self.hand.remove(card)
            # Implement card effect here
            # For now, just discard the card
            self.discard_pile.append(card)
        else:
            print("Card not in hand")

    def buy_card(self, card, supply):
        # Buy a card from the supply
        if supply.buy(card.name):
            self.discard_pile.append(card)
        else:
            print("Card not available for purchase")
