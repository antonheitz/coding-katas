from dataclasses import dataclass
import random
from typing import List

@dataclass
class Card:
    color: str
    value: int

@dataclass
class Player:
    id: int
    cards: List[Card]

def play(players: List[Player]) -> int:
    return 0

def game(random_seed: int = None):
    # create stash
    stash: List[str] = []
    for color in ["><", "->", "<3", "<>"]:
        for value in range(1, 14):
            stash.append(Card(color, value))
    # create players and deal cards
    player_one: Player = Player(1, [])
    player_two: Player = Player(2, [])
    if random_seed:
        random.seed(random_seed)
    random.shuffle(stash)
    cards_per_player: int = int(len(stash)/2)
    player_one.cards = stash[0:cards_per_player]
    player_two.cards = stash[cards_per_player:]
    print(f"The winnder is {play([player_one, player_two])}")

game()
#game(10)
#game(15)
#game(20)
#game(25)
