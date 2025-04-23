class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        non_overlapping = 0
        prev_end = float('-inf')
        for start, end in intervals:
            if start >= prev_end:
                non_overlapping += 1
                prev_end = end
        return len(intervals) - non_overlapping

# TC : O(NlogN)
# SC : O(1)