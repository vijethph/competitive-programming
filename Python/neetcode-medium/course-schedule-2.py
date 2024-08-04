# https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort - run DFS on each node
        # build adjacency list of prereqs
        prereq = { c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states: visited - added to output,
        # visiting - not added to output, but added to cycle and unvisited - not added to output or cycle
        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output