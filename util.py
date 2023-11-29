from card import VictoryCard

def setup_supply(card_list):
    # Set up the initial supply of cards
    # card_list should be a list of tuples (Card, count)
    supply = {}
    for card, count in card_list:
        supply[card.name] = (card, count)
    return supply

def calculate_victory_points(player):
    # Calculate the victory points for a player
    victory_points = 0
    for card in player.deck.cards + player.discard_pile:
        if isinstance(card, VictoryCard):
            victory_points += card.points
    return victory_points
