class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#"  + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        N = len(s)
        res = []
        print(s)
        while i < N:
            length = 0
            left = i
            while s[i].isnumeric():
                i += 1
            length = int((s[left:i])) if i > left else 0
            i -= 1
            res.append(s[i + 2: i + 2 + length])
            i += 2 + length
        return res
