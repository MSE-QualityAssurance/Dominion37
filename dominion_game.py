from supply import Supply
from player import Player

class DominionGame:
    def __init__(self, players, supply):
        self.players = players
        self.supply = supply
        self.current_player_index = 0

    def setup_game(self):
        # Example setup; you'll need to define the starting decks and supply setup
        for player in self.players:
            player.deck.setup_starting_deck()  # Assuming this method sets up the starting deck
        # Set up the supply with initial cards
        self.supply.setup_initial_supply()

    def play_game(self):
        # Main game loop
        while not self.is_game_over():
            self.play_turn(self.players[self.current_player_index])
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.end_game()

    def play_turn(self, player):
        # Example turn structure
        player.draw_hand()
        player.print_status()
        # Implement action phase (for now, skipping)
        # Implement buy phase
        # Example: let player buy one card
        if len(self.supply.available_cards) > 0:
            card_name = list(self.supply.available_cards.values())[0][0]  # Example: buying the first available card
            player.buy_card(card_name, self.supply)
        # Clean up phase
        player.discard_hand()
        player.draw_hand()

    def is_game_over(self):
        # Check game end conditions
        # Example: game ends when a certain card pile is empty
        return any(count == 0 for card, count in self.supply.available_cards.values())

    def end_game(self):
        # Calculate points and declare winner
        winner = max(self.players, key=lambda p: p.calculate_points())
        print(f"Winner is {winner.name}")

# Add other methods as needed, such as calculating points, handling actions, etc.
