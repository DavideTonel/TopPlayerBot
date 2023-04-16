from .soccer_config import *
from .Player import Player

class Match:
    def __init__(self, player1 : Player, player2 : Player, score_player1, score_player2):
        self.p1 = player1
        self.p2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2

        self.p1.updateStatistics(goal_scored = self.score_player1, goal_received = self.score_player2)
        self.p2.updateStatistics(goal_scored = self.score_player2, goal_received = self.score_player1)
        self.updateScore()
    
    def __str__(self):
        return str(self.player1.name) + ' ' + str(self.score_player1) + ' - ' + str(self.score_player2) + ' ' + str(self.player2.name)

    def updateScore(self):
        if self.score_player1 > self.score_player2:
            self.p1.updateScore(WIN_POINTS)
            self.p2.updateScore(DEFEAT_POINTS)
        elif self.score_player1 < self.score_player2:
            self.p1.updateScore(DEFEAT_POINTS)
            self.p2.updateScore(WIN_POINTS)
        else:
            self.p1.updateScore(DRAW_POINTS)
            self.p2.updateScore(DRAW_POINTS)


class MatchBuilder:
    def __init__(self):
        self.p1 = None
        self.p2 = None
        self.score_player1 = None
        self.score_player2 = None

    def setPlayer1(self, player1 : Player) -> None:
        self.p1 = player1

    def setPlayer2(self, player2 : Player) -> None:
        if self.p1.name == player2.name:
            raise Exception(self.p1.name + ' non può scontrarsi con sè stesso')
        self.p2 = player2

    def setScorePlayer1(self, score_player1 : int) -> None:
        self.score_player1 = score_player1

    def setScorePlayer2(self, score_player2 : int) -> None:
        self.score_player2 = score_player2

    def build(self) -> Match:
        return Match(self.p1, self.p2, self.score_player1, self.score_player2)
