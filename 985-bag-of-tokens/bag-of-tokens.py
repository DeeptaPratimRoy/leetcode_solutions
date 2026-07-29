class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        max_score = 0
        score = 0
        left = 0
        right = len(tokens)-1
        while left<=right:
            if power>= tokens[left]:
                power -= tokens[left]
                score+=1
                left+=1
                max_score = max(score,max_score)
            elif score > 0:
                power+= tokens[right]
                score-=1
                right-=1
            else:
                break
        return max_score

        
        