from numpy.random import randint
from random import sample

class Round:
    def __init__(self, ui, players, startingPlayer):
        self.players = players
        self.nPlayers = len(players)
        self.startingPlayer = startingPlayer

        # distribute cards to players
        self.cardsPerPlayer = 22 // self.nPlayers
        shuffledCards = sample(range(22), 22)[:self.cardsPerPlayer * self.nPlayers]
        for i in range(self.nPlayers):
            self.players[i].assignCards(shuffledCards[i*self.cardsPerPlayer:(i+1) * self.cardsPerPlayer])

    def play(self):
        pass