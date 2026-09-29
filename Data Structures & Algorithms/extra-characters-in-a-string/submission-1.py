class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)
        
        # dp[i] = min extra chars in s[0:i]
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # Option 1: s[i-1] is an extra character
            dp[i] = dp[i - 1] + 1
            
            # Option 2: s[j:i] matches a word in the dictionary
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[n]