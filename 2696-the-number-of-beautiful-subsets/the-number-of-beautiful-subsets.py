from collections import Counter
class Solution(object):
    def beautifulSubsets(self, nums, k):
        ans =[0]
        freq = Counter()
        def backtrack(index,subset):
            if index == len(nums):
                if len(subset) != 0:
                    ans[0]+=1
                return
            x = nums[index]
            if freq[x-k] == 0 and freq[x+k] == 0:
                freq[x]+=1
                subset.append(x)
                backtrack(index+1,subset)
                subset.pop()
                freq[x]-=1
            backtrack(index+1,subset)
        backtrack(0,[])
        return ans[0]
