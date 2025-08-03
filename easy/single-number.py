class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        d = {}
        
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        
        v = 1
        k = ''        
        for i in d:
            if d[i] <= v:
                k = i
            
        return k
    
sol = Solution()

print(sol.singleNumber([2,2,1]))
print(sol.singleNumber([4,1,2,1,2]))
print(sol.singleNumber([1]))