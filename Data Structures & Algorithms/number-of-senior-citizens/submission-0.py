class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        
        for detail in details:
            start = len(detail) - 4
            end = start + 2
            age = int(detail[start:end])
            if age > 60:
                res += 1
        return res