class Solution(object):
    def maxArea(self, h):
        i,j,maxA=0,len(h)-1,0
        while i<j:
            maxA=max(maxA,(j-i)*min(h[i],h[j]))
            if h[i]<h[j] :
                i+=1
            else:
                j-=1
        return maxA
