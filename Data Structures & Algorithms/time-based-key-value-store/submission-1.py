class TimeMap:

    def __init__(self):
        self.time_map = {}
        # key -> (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_map.get(key, [])
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            value, time = values[mid]
            if time <= timestamp:
                res = value
                left = mid + 1
            else:
                right = mid - 1
        return res
        
