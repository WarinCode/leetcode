class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        
        nums.append(target)
        nums.sort()
        return nums.index(target)
    
sol = Solution()

print(sol.searchInsert([1,3,5,6], 5))
print(sol.searchInsert([1,3,5,6], 2))
print(sol.searchInsert([1,3,5,6], 7))