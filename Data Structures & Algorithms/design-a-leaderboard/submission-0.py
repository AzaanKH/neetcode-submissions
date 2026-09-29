class Leaderboard:

    def __init__(self):
        self.id_score = {}
        self.score = {}

    def addScore(self, playerId: int, score: int) -> None:
        prevScore = 0
        if playerId in self.id_score:
            # remove from old score
            prevScore = self.id_score[playerId]
            self.remove(playerId)
        newScore = prevScore + score
        self.id_score[playerId] = newScore
        if newScore not in self.score:
            self.score[newScore] = []
        self.score[newScore].append(playerId)

    def remove(self, playerId: int) -> None:
        prevScore = self.id_score[playerId]
        self.score[prevScore].remove(playerId)
        if not self.score[prevScore]:
            del self.score[prevScore]


    def top(self, K: int) -> int:
        scoreSum = 0
        for key in sorted(self.score, reverse=True):
            for _ in self.score[key]:
                scoreSum += key
                K -= 1
                if K == 0:
                    return scoreSum
        return scoreSum
        

    def reset(self, playerId: int) -> None:
        self.remove(playerId)
        del self.id_score[playerId]   
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
