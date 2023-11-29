from player import Player
from supply import Supply
from dominion_game import DominionGame

def main():
    # Create players (for simplicity, using 2 players)
    player1 = Player("Alice")
    player2 = Player("Bob")

    # Set up the supply
    supply = Supply()  # You'll define the setup in the Supply class

    # Create the game instance
    game = DominionGame([player1, player2], supply)

    # Start the game
    game.play_game()

if __name__ == "__main__":
    main()
