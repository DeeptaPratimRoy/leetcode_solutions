from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq=defaultdict(int)
        left= 0
        ans= 0
        n=len(s) 
        for right in range(n):
            freq[s[right]]+=1
            while freq[s[right]]>1:
                freq[s[left]]-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans