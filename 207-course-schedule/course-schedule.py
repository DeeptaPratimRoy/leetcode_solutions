from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            for new_course in graph[course]:
                indegree[new_course] -= 1
                if indegree[new_course] == 0:
                    queue.append(new_course)
        return count == numCourses
