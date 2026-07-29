class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        new = []
        left = 0
        right = len(people)-1
        while left<=right:
            if people[left]+people[right]<=limit:
                new.append([people[left],people[right]])
                left+=1
                right-=1
            else:
                new.append(people[right])
                right-=1
        return len(new)