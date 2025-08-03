class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = [*nums1, *nums2]
        nums3.sort()
        
        l = len(nums3)
        mid = int(l / 2)
        if l % 2 != 0:
            return nums3[mid]
        
        median = (nums3[mid - 1] + nums3[mid]) / 2
        return median

sol = Solution()

print(sol.findMedianSortedArrays([1, 3], [2]))
print(sol.findMedianSortedArrays([1, 2], [3, 4]))                