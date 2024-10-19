class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        col = len(matrix[0])
        row = len(matrix)
        l = 0
        r = row * col - 1

        while l <= r:
            mid = (l + r) // 2

            col_index = mid % col
            row_index = mid // col

            if matrix[row_index][col_index] == target:
                return True
            elif matrix[row_index][col_index] < target:
                l =  mid + 1
            else:
                r = mid - 1
        return False




solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))