from dominion_game import DominionGame
from player import Player
from supply import Supply

def main():
    # Create players
    player1 = Player("Alice")
    player2 = Player("Bob")
    players = [player1, player2]

    # Set up the supply
    # Example setup; actual setup will depend on your game rules
    supply = Supply({"Gold": (None, 30), "Estate": (None, 14)})

    # Create the game instance
    game = DominionGame(players, supply)
    game.setup_game()

    # Start the game
    game.play_game()

if __name__ == "__main__":
    main()