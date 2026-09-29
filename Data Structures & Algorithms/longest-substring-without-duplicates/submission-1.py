class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        left = 0
        res = 0
        for r in range(len(s)):
            while check and s[r] in check:
                check.remove(s[left])
                left += 1
            check.add(s[r])
            res = max(r - left + 1, res)
        return res
