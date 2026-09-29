class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check_palidrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        delete = False
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return check_palidrome(left + 1, right) or check_palidrome(left, right - 1)
            left += 1
            right -= 1
        return True