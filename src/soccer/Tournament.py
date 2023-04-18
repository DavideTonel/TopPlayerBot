from .Player import Player
from .Match import Match
from typing import List


class Tournament:
    def __init__(self):
        self.players = {}
        self.matches:List[Match] = []

    def setPlayers(self, names : set):
        for name in names:
            self.players[name] = Player(name)

    def addMatch(self, match : Match):
        self.matches.append(match)
    def getMatches(self):
        return self.matches
    def getRanking(self) -> list:
        if (len(self.matches) <= 0):
            return []
        playersInRanking = list(self.players.values())
        playersInRanking.sort(reverse=True)
        return playersInRanking
    
    def getPlayerNames(self) -> list:
        return self.players.keys()
    
    def getPlayerByName(self, name : str) -> Player:
        return self.players[name]
    
    def reset(self) -> None:
        self.players = {}
        self.matches = []
