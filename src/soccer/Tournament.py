from .Player import Player
from .Match import Match
from typing import List
import itertools

class Tournament:
    def __init__(self, names):
        self.players = {}
        self.matches:List[Match] = []
        for name in names:
            self.players[name] = Player(name)
        self.matchesLeft = list(itertools.combinations(names, 2))

    def addMatch(self, match : Match):
        self.matches.append(match)
        if (match.getPlayer1().getName(),match.getPlayer2().getName()) in self.matchesLeft:
            self.matchesLeft.remove((match.getPlayer1().getName(),match.getPlayer2().getName()))
        if (match.getPlayer2().getName(),match.getPlayer1().getName()) in self.matchesLeft:
            self.matchesLeft.remove((match.getPlayer2().getName(),match.getPlayer1().getName()))
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
    def getMatchesLeft(self) -> List[Match]:
        return self.matchesLeft
    def reset(self) -> None:
        self.players = {}
        self.matches = []
