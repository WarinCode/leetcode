class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        left = str(x)
        right = ''    
        for char in reversed(left):
            right += char
            
        return left == right

sol = Solution()

print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))