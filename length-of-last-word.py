class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = s.strip().split(' ')
        return len(li[len(li) - 1])
        
sol = Solution()

print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
print(sol.lengthOfLastWord("luffy is still joyboy"))