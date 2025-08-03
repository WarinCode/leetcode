class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = ''
        for digit in digits:
            result += str(digit)
        result = list(int(i) for i in str(int(result) + 1))
        return result
        
sol = Solution()

print(sol.plusOne([1,2,3]))
print(sol.plusOne([4,3,2,1]))
print(sol.plusOne([9]))