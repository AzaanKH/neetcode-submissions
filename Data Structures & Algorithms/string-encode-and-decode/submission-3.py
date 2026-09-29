class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for c in strs:
            res += str(len(c)) + '#' + c
        return res

    def decode(self, s: str) -> List[str]:
        N = len(s)
        res = []
        i = 0
        while i < N:
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            res.append(s[j + 1 : j + 1 + num])
            i = j + 1 + num
        return res
