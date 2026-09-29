class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row_check = {}
        col_check = {}
        ROWS, COLS = len(picture), len(picture[0])
        for r in range(ROWS):
            for c in range(COLS):
                if picture[r][c] == 'B':
                    if r not in row_check:
                        row_check[r] = [0, c]
                    if c not in col_check:
                        col_check[c] = [0, r]
                    row_check[r][0] += 1
                    col_check[c][0] += 1
                    
        res = 0
        # print(row_check)
        for key in row_check:
            count, c = row_check[key]
            if count == 1 and col_check[c][0] == 1:
                res += 1
        return res