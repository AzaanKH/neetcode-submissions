class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        N = len(text1)
        M = len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        # N is columns text 1
        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if text1[c] == text2[r]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        print(dp)
        return dp[0][0]
        