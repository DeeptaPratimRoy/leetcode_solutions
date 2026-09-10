class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph =[[] for _ in range(numCourses)]
        indegree = [0]* numCourses
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course]+=1
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        result =[]
        while queue:
            course = queue.popleft()
            result.append(course)
            for nei in graph[course]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        if len(result) == numCourses:
            return result
        else:
            return []
            