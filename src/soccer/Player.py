class Player:
    def __init__(self, name : str):
        self.name = name
        self.totalGoalScored = 0
        self.totalGoalReceived = 0
        self.score = 0

    def __str__(self):
        return  'Name: ' + str(self.name) + '\t' \
                'Total Goal: ' + str(self.totalGoalScored) + '\t' \
                'Goal Received: ' + str(self.totalGoalReceived) + '\t' \
                'Score: ' + str(self.score)
    
    def __lt__(self, other):
        if self.score < other.score:
            return True
        elif self.score > other.score:
            return False
        else:
            if self.getGoalDifference() < other.getGoalDifference():
                return True
            else:
                return False
        

    def updateStatistics(self, goalScored : int, goalReceived : int):
        self.totalGoalScored += goalScored
        self.totalGoalReceived += goalReceived

    def updateScore(self, score : int):
        self.score += score

    def getGoalDifference(self):
        return self.totalGoalScored - self.totalGoalReceived

    def getName(self) -> str:
        return self.name
