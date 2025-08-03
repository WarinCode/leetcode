class Solution:
    def sortColors(self, nums: list[int]) -> None:
        arr = []
        arr2 = []
        arr3 = []
        
        for n in nums:
            if n == 0:
                arr.append(n)
            elif n == 1:
                arr2.append(n)
            elif n == 2:
                arr3.append(n)
                
        nums.clear()
        nums.extend(arr)
        nums.extend(arr2)
        nums.extend(arr3)
        
        return nums
    
sol = Solution()

print(sol.sortColors([2,0,2,1,1,0]))
print(sol.sortColors([2,0,1]))