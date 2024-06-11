class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: # no prereqs for any course
            return True

        coursesToPrereqs = [[] for i in range(numCourses)]

        # build adjacency list for graph
        for c, p in prerequisites:
            coursesToPrereqs[c].append(p)

        visited = set()

        # iterate over each courses to see if it can be finished
        for c in range(numCourses):
            if not self._canFinish(c, visited, coursesToPrereqs, []):
                return False

        return True

    def _canFinish(self, course, visited, coursesToPrereqs, path) -> bool:
        if course in visited:
            if course in path: # cycle
                return False
            else: # already processed
                return True

        # mark in dfs as finished to avoid re-processing
        visited.add(course)
        # add to current path to check
        path.append(course)

        # check all prereqs if they can be finished
        for p in coursesToPrereqs[course]:
            if not self._canFinish(p, visited, coursesToPrereqs, path):
                return False
        
        path.pop() # remove current node from path since we can finish it
        return True
                
