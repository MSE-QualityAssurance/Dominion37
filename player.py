from deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.hand = []
        self.discard_pile = []
        self.coins = 0  # Track the number of coins a player has
        self.actions = 1  # Track the number of actions a player can perform

    def draw_card(self):
        # Draw a single card from the deck
        if len(self.deck.cards) == 0:
            self.deck.reshuffle_from_discard(self.discard_pile)
        card = self.deck.draw()
        if card:
            self.hand.append(card)

    def draw_hand(self, num_cards=5):
        # Draw a number of cards from the deck
        for _ in range(num_cards):
            self.draw_card()

    def add_coins(self, amount):
        # Add coins to the player's total
        self.coins += amount

    def add_actions(self, amount):
        # Add actions to the player's total
        self.actions += amount

    def play_card(self, card):
        # Play a card from hand
        if card in self.hand:
            self.hand.remove(card)
            card.play(self)  # The card's play method is called here
            self.discard_pile.append(card)
        else:
            print("Card not in hand")

    def buy_card(self, card, supply):
        # Buy a card from the supply
        purchased_card = supply.buy(card.name)
        if purchased_card:
            self.discard_pile.append(purchased_card)
        else:
            print("Card not available for purchase")

    def discard_hand(self):
        # Discard the current hand to the discard pile
        self.discard_pile.extend(self.hand)
        self.hand.clear()

    def reshuffle_discard_into_deck(self):
        # Reshuffle discard pile into the deck
        self.deck.reshuffle_from_discard(self.discard_pile)
        self.discard_pile.clear()
