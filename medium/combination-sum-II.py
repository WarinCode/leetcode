# class Solution(object):
#     def morethan_target(self, candidates, target):
#         for n in candidates:
#             if n > target:
#                 candidates.remove(n)
                
#         return candidates
        
#     def combinationSum2(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         arr2 = []
#         candidates = self.morethan_target(candidates, target)
    
#         for i in range(len(candidates)):
#             s = candidates[i]
#             arr = []
#             arr.append(candidates[i])
            
#             if s == target:
#                 if [s] not in arr2:
#                     arr2.append([s])

#             for j in range(len(candidates)):
#                 if candidates[i] == candidates[j] and i == j:
#                     continue
                
#                 s += candidates[j]
#                 arr.append(candidates[j])
#                 # print(f'arr = {arr}')
#                 # print(f'sum = {s}')

#                 if s == target:
#                     arr.sort()
#                     if arr not in arr2:
#                         arr2.append(arr.copy())
#                         arr.clear()
#                         break
                
#                 if s > target:
#                     arr.pop()
#                     s = sum(arr)
                                
#             for k in range(len(candidates)):
#                 for v in range(len(candidates)):
#                     n1 = candidates[k]
#                     n2 = candidates[v]
#                     if candidates[k] == candidates[v] and k == v:
#                         continue                    
                    
#                     if (n1 + n2) == target:
#                         arr = [candidates[k], candidates[v]]
#                         arr.sort()
#                         if arr not in arr2:
#                             arr2.append(arr)
#         return arr2
        
        
# sol = Solution()

# print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
# print(sol.combinationSum2([2,5,2,1,2], 5))
# print(sol.combinationSum2([1,1], 1))