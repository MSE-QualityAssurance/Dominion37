class Card:
    def __init__(self, name, cost, card_type):
        self.name = name
        self.cost = cost
        self.card_type = card_type  # Action, Treasure, Victory

class ActionCard(Card):
    def __init__(self, name, cost, effects):
        super().__init__(name, cost, "Action")
        self.effects = effects

    def play(self, player, game):
        # Implement the effects of the card

class TreasureCard(Card):
    # Implementation for Treasure cards

class VictoryCard(Card):
    # Implementation for Victory cards
