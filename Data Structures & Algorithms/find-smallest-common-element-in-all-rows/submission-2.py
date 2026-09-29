class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        count = [0] * 10001
        ROWS, COLS = len(mat), len(mat[0])
        for r in range(ROWS):
            for c in range(COLS):
                count[mat[r][c]] += 1
                if count[mat[r][c]] == ROWS:
                    return mat[r][c]
        return -1