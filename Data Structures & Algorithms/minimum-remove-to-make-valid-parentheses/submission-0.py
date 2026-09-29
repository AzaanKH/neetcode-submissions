class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_count = 0
        res = []
        for c in s:
            if c == '(':
                left_count += 1
            elif c == ')':
                if left_count == 0:
                    continue
                left_count -= 1
            res.append(c)
        right = len(res) - 1
        while left_count > 0:
            if res[right] == '(':
                res[right] = ''
                left_count -= 1
            right -= 1
        return "".join(res)