from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t):
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)