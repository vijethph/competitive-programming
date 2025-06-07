# https://leetcode.com/problems/course-schedule-iv/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)
        
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()

                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq) # union
                
                prereqMap[crs].add(crs)
            
            return prereqMap[crs]
        
        prereqMap = {} # map crs -> hashset of indirect prereqs

        for crs in range(numCourses):
            dfs(crs)
        
        res = []

        for u, v in queries:
            res.append(u in prereqMap[v])
        return res