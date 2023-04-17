from .soccer_config import *
from .Player import Player


class Match:
    def __init__(self, player1: Player, player2: Player, scorePlayer1, scorePlayer2):
        self.p1 = player1
        self.p2 = player2
        self.scorePlayer1 = scorePlayer1
        self.scorePlayer2 = scorePlayer2

        self.p1.updateStatistics(
            goalScored=self.scorePlayer1, goalReceived=self.scorePlayer2
        )
        self.p2.updateStatistics(
            goalScored=self.scorePlayer2, goalReceived=self.scorePlayer1
        )
        self.updateScore()

    def __str__(self):
        return (
            str(self.player1.name)
            + " "
            + str(self.scorePlayer1)
            + " - "
            + str(self.scorePlayer2)
            + " "
            + str(self.player2.name)
        )

    def updateScore(self):
        if self.scorePlayer1 > self.scorePlayer2:
            self.p1.updateScore(WIN_POINTS)
            self.p2.updateScore(DEFEAT_POINTS)
        elif self.scorePlayer1 < self.scorePlayer2:
            self.p1.updateScore(DEFEAT_POINTS)
            self.p2.updateScore(WIN_POINTS)
        else:
            self.p1.updateScore(DRAW_POINTS)
            self.p2.updateScore(DRAW_POINTS)
    
    def getPlayer1(self):
        return self.p1

    def getPlayer2(self):
        return self.p2


class MatchBuilder:
    def __init__(self):
        self.p1 = None
        self.p2 = None
        self.scorePlayer1 = None
        self.scorePlayer2 = None

    def setPlayer1(self, player1: Player) -> None:
        self.p1 = player1

    def setPlayer2(self, player2: Player) -> None:
        if self.p1.name == player2.name:
            raise Exception(self.p1.name + " non può scontrarsi con sè stesso")
        self.p2 = player2

    def setScorePlayer1(self, scorePlayer1: int) -> None:
        self.scorePlayer1 = scorePlayer1

    def setScorePlayer2(self, scorePlayer2: int) -> None:
        self.scorePlayer2 = scorePlayer2

    def build(self) -> Match:
        return Match(self.p1, self.p2, self.scorePlayer1, self.scorePlayer2)
