class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        left = 0

        for r in range(len(s) + 1):
            if r == len(s) or s[r] == " ":
                right = r - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                left = r + 1