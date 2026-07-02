class Solution(object):
    def restoreIpAddresses(self, s):
        ans= []
        def backtrack(index,subset):
            if len(subset) == 4:
                if index == len(s):
                    ans.append(".".join(subset))
                return
            for length in range(1,4):
                if index+length>len(s):
                    return
                substring = s[index:index+length]
                if len(substring)>1 and substring[0] == "0":
                    continue
                if int(substring)>255:
                    continue
                subset.append(substring[:])
                backtrack(index+length,subset)
                subset.pop()
        backtrack(0,[])
        return ans
        



        