class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        if s == t:
            return False
        ns, nt = len(s), len(t)
        for i in range(min(ns, nt)):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                elif ns < nt:
                    return s[i:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]
        return abs(ns - nt) == 1