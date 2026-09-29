class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        check = set()

        for r in range(len(s)):
            if s[r] in check:
                while s[r] in check:
                    check.remove(s[left])
                    left += 1
            check.add(s[r])
            res = max(r - left + 1, res)
        return res        