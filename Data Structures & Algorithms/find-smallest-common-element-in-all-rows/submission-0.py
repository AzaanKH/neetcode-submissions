class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        i = 0
        res = float('inf')
        left, right = 0, max(max(row) for row in mat)
        new_mat = []
        for i in range(len(mat)):
            new_mat.append(set(mat[i]))
        
        def common_element(point):
            for i in range(len(new_mat)):
                if point not in new_mat[i]:
                    return False
            return True
        while left <= right:
            mid = (left + right) // 2
            if common_element(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res if res != float('inf') else - 1
