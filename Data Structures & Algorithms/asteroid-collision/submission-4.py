class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for asteriod in asteroids:
            while res and res[-1] > 0 and asteriod < 0:
                prev_asteriod = res[-1]
                diff = prev_asteriod + asteriod
                if diff > 0:
                    asteriod = 0
                    break
                elif diff < 0:
                    res.pop()
                else:
                    asteriod = 0
                    res.pop()
                    break
            if asteriod != 0:
                res.append(asteriod)
        return res 