class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for c in strs:
            s += str(len(c)) + "#" + c
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        N = len(s)
        while i < N:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length 
        return res