class Solution(object):
    def subsetsWithDup(self, nums):
        ans = []
        nums.sort()
        def backtrack(index,subset):
                ans.append(subset[:])
                for i in range(index,len(nums)):
                    if i>index and nums[i-1] == nums[i]:
                        continue
                    subset.append(nums[i])
                    backtrack(i+1,subset)
                    subset.pop()
        backtrack(0,[])
        return ans
            
        