class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]
        for n in nums:
            if n < min:
                min = n
        
        return min
        
sol = Solution()

print(sol.findMin([1,3,5]))
print(sol.findMin([2,2,2,0,1]))