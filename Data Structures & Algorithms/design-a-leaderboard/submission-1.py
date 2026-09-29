from sortedcontainers import SortedList
class Leaderboard:

    def __init__(self):
        self.id_score = {}
        self.scores = SortedList()
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.id_score:
            self.scores.remove(self.id_score[playerId])
        self.id_score[playerId] = self.id_score.get(playerId, 0) + score
        self.scores.add(self.id_score[playerId])
            

    


    def top(self, K: int) -> int:
        return sum(self.scores[-K:])

    def reset(self, playerId: int) -> None:
        self.scores.remove(self.id_score[playerId])
        del self.id_score[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
