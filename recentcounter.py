from collections import deque
class RecentCounter:

    def __init__(self, timeframe: int):
        self.requests = deque()
        self.timeframe = timeframe

    def ping(self, t: int) -> int:
        while len(self.requests)>0 and t-self.requests[0]>self.timeframe:
            self.requests.popleft()
        self.requests.append(t)
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
        
myobj = RecentCounter(3000)
print(myobj.ping(642))
print(myobj.ping(1849))
print(myobj.ping(4921))
print(myobj.ping(5936))
print(myobj.ping(5957))