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
        for effect in self.effects:
            effect(player, game)

# Example Action Cards
class Smithy(ActionCard):
    def __init__(self):
        super().__init__("Smithy", 4, [self.draw_cards])

    @staticmethod
    def draw_cards(player, game):
        for _ in range(3):
            player.draw_card()

class Village(ActionCard):
    def __init__(self):
        super().__init__("Village", 3, [self.draw_card, self.add_actions])

    @staticmethod
    def draw_card(player, game):
        player.draw_card()

    @staticmethod
    def add_actions(player, game):
        player.add_actions(2)

class TreasureCard(Card):
    def __init__(self, name, cost, value):
        super().__init__(name, cost, "Treasure")
        self.value = value

    def play(self, player, game):
        player.add_coins(self.value)

# Example Treasure Cards
class Copper(TreasureCard):
    def __init__(self):
        super().__init__("Copper", 0, 1)

class Silver(TreasureCard):
    def __init__(self):
        super().__init__("Silver", 3, 2)

class Gold(TreasureCard):
    def __init__(self):
        super().__init__("Gold", 6, 3)

class VictoryCard(Card):
    def __init__(self, name, cost, points):
        super().__init__(name, cost, "Victory")
        self.points = points

    def play(self, player, game):
        # Victory cards usually don't have an in-game effect
        pass

# Example Victory Cards
class Estate(VictoryCard):
    def __init__(self):
        super().__init__("Estate", 2, 1)

class Duchy(VictoryCard):
    def __init__(self):
        super().__init__("Duchy", 5, 3)

class Province(VictoryCard):
    def __init__(self):
        super().__init__("Province", 8, 6)

