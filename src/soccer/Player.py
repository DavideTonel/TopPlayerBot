class Player:
    def __init__(self, name : str):
        self.name = name
        self.total_goal_scored = 0
        self.total_goal_received = 0
        self.score = 0

    def __str__(self):
        return  'Name: ' + str(self.name) + '\t' \
                'Total Goal: ' + str(self.total_goal_scored) + '\t' \
                'Goal Received: ' + str(self.total_goal_received) + '\t' \
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
        

    def updateStatistics(self, goal_scored : int, goal_received : int):
        self.total_goal_scored += goal_scored
        self.total_goal_received += goal_received

    def updateScore(self, score : int):
        self.score += score

    def getGoalDifference(self):
        return self.total_goal_scored - self.total_goal_received

    def getName(self) -> str:
        return self.name
