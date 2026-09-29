class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search the correct row
        leftRow, rightRow = 0, len(matrix) - 1
        row = -1
        while leftRow <= rightRow:
            mid = (rightRow + leftRow) // 2
            if matrix[mid][-1] < target:
                leftRow = mid + 1
            elif matrix[mid][0] > target:
                rightRow = mid - 1
            elif matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
        print(row)
        if row == -1:
            return False
        
        leftCol, rightCol = 0, len(matrix[0]) - 1
        while leftCol <= rightCol:
            mid = (rightCol + leftCol) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                rightCol = mid - 1
            else:
                leftCol = mid + 1
        return False
        