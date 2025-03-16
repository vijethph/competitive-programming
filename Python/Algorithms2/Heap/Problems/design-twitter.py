# https://leetcode.com/problems/design-twitter/description/

class Twitter:

    def __init__(self):
        self.count = 0 # count represents time at which tweet was posted
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # negative values due to min heap being used as max heap

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from recent
        minHeap = []

        self.followMap[userId].add(userId) # user might post a tweet themselves
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap: # if user has posted atleast 1 tweet
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        
        heapq.heapify(minHeap)
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
            
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        # use hashset for follow and unfollow - inserts and removes elements in O(1) time
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)