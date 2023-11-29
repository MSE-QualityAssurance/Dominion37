class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.hand = []
        self.discard_pile = []

    def draw_hand(self):
        # Draw cards from the deck

    def play_card(self, card):
        # Play a card from hand

    def buy_card(self, card):
        # Buy a card from the supply
