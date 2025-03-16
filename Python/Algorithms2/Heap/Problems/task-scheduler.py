# https://leetcode.com/problems/task-scheduler/description/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # using max heap and a queue - O(n)

        count = Counter(tasks) # hashmap which stores frequencies of elements of a list
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        que = deque() # pairs of [-cnt, idleTime]

        while maxHeap or que:
            time += 1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # time taken right now for the task
                if cnt:
                    que.append([cnt, time + n]) # next available time
                
            if que and que[0][1] == time:
                heapq.heappush(maxHeap, que.popleft()[0])
        
        return time




