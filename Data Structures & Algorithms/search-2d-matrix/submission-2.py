class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowRow = 0
        highRow = len(matrix) - 1
        row = -1  # Initialize row to an invalid value
        
        while lowRow <= highRow:
            mid = (highRow + lowRow) // 2
            if matrix[mid][0] > target:
                highRow = mid - 1
            elif matrix[mid][-1] < target:
                lowRow = mid + 1
            else:
                row = mid
                break
        
        # If the row is not found
        if row == -1:
            return False

        # Binary search within the row to find the target
        lowCol, highCol = 0, len(matrix[0]) - 1
        while lowCol <= highCol:
            mid = (highCol + lowCol) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lowCol = mid + 1
            else:
                highCol = mid - 1
        
        return False

        