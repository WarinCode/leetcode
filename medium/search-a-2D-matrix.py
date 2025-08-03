class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            for col in row:
                if col == target:
                    return True

        return False
        
sol = Solution()

print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))