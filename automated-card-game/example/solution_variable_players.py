from dataclasses import dataclass
import random
import math
from typing import List

@dataclass
class Card:
    color: str
    value: int

@dataclass
class Player:
    id: int
    cards: List[Card]

    def deal_card(cls) -> Card:
        if not len(cls.cards):
            raise PlayerLostException(cls.id)
        return cls.cards.pop(0)
    
@dataclass
class BattleStash:
    cards: List[Card]

    def deal_cards(cls, players: List[Player], iterations: int = 1) -> None:
        for i in range(iterations):
            for player in players:
                try:
                    cls.cards.append(player.deal_card())
                except PlayerLostException as e:
                    players = [player for player in players if e.looser_id != player.id]
        if len(players) == 1:
            raise PlayerWonException(players[0])

    def check_winner(cls, players: List[Player]) -> int:
        current_battle_values: List[int] = [card.value for card in cls.cards[len(cls.cards) - len(players):]]
        winning_value: int = max(current_battle_values)
        if len([value for value in current_battle_values if value == winning_value]) > 1:
            return -1
        return players[current_battle_values.index(winning_value)].id
    
    def reward_winner(cls, players: List[Player], id: int) -> None:
        for player in players:
            if player.id == id:
                player.cards += cls.cards
        cls.cards = []

class PlayerLostException(Exception):
    def __init__(self, looser_id: int):
        super().__init__(f"Player {looser_id} lost!")
        self.looser_id = looser_id

class PlayerWonException(Exception):
    def __init__(self, winner: Player):
        super().__init__(f"Player {winner.id} won!")
        self.winner = winner

def play(players: List[Player]) -> int:
    players.sort(key=lambda x: x.id)
    battle_stash: BattleStash = BattleStash([])
    while True:
        try:
            battle_stash.deal_cards(players)
            winner_id: int = battle_stash.check_winner(players)
            while winner_id < 0:
                battle_stash.deal_cards(players, 4)
                winner_id = battle_stash.check_winner(players)
            battle_stash.reward_winner(players, winner_id)
        except PlayerWonException as e:
            return e.winner.id

def game(random_seed: int = None, player_count: int = 2):
    # create stash
    stash: List[str] = []
    for color in ["><", "->", "<3", "<>"]:
        for value in range(1, 14):
            stash.append(Card(color, value))
    # create players
    players: List[Player] = [Player(player_id, []) for player_id in range(player_count)]
    # shuffle cards (with seed if necessary)
    if random_seed:
        random.seed(random_seed)
    random.shuffle(stash)
    # deal cards to players
    cards_per_player: int = [int(len(stash)/player_count) for player_id in range(player_count)]
    overrun: int = len(stash) - sum(cards_per_player)
    for extra_card_player in range(overrun):
        cards_per_player[extra_card_player] += 1
    for index, player in enumerate(players):
        player.cards = stash[0:cards_per_player[index]]
        stash = stash[cards_per_player[index]:]
    print(f"The winner for Seed {random_seed} with {player_count} Players is {play(players)}")

[game(i) for i in [10, 15, 21, 25, 30, 35, 40]]
#[game(random_seed=i, player_count=3) for i in [10, 15, 21, 25]]
#[game(random_seed=i, player_count=5) for i in [10, 15, 21, 25]]
#[game(random_seed=i, player_count=7) for i in [10, 15, 21, 25]]
#[game(random_seed=i, player_count=9) for i in [10, 15, 21, 25]]
