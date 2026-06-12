from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        mp=Counter(p)
        count=len(mp)
        left = 0
        ans= []
        n=len(p)
        k=len(s)
        for right in range(k):
            if s[right] in mp:
                mp[s[right]]-=1
                if mp[s[right]] == 0:
                    count-=1
            if right-left+1 == n:
                if count == 0:
                    ans.append(left)
                if s[left] in mp:
                    if mp[s[left]]==0:
                        count+=1
                    mp[s[left]]+=1
                left+=1  
        return ans