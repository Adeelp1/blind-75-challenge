from heapq import heappush, heappushpop
class MedianFinder:

    def __init__(self):
        self.l_heap = []
        self.r_heap = []

    def addNum(self, num: int) -> None:
        if len(self.l_heap) == len(self.r_heap):
            r_num = heappushpop(self.r_heap, num)
            heappush(self.l_heap, -r_num)
        else:
            l_num = heappushpop(self.l_heap, -num)
            heappush(self.r_heap, -l_num)

    def findMedian(self) -> float:
        if len(self.l_heap) == len(self.r_heap):
            return ((-self.l_heap[0]) + self.r_heap[0]) /2
        else:
            return -self.l_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# TC : O(LogN)
# SC : O(N)