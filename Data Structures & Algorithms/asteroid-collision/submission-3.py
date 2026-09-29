class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        n = len(asteroids)
        for i in range(n):
            asteroid = asteroids[i]
            while res and res[-1] > 0 and asteroid < 0:
                prev_asteroid = res[-1]
                diff = prev_asteroid + asteroid
                if diff < 0:
                    res.pop()
                elif diff > 0:
                    asteroid = 0
                else:
                    asteroid = 0
                    res.pop()
            if asteroid != 0:
                res.append(asteroid)
        return res

        