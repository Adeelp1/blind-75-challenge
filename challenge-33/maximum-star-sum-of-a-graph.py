import heapq
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # build edges for each value : [for each index: [value of neighbors]]
        neighbors = [[] for _ in vals]
        
        for left, right in edges:
            neighbors[left].append(-vals[right])
            neighbors[right].append(-vals[left])

        for sublist in neighbors:
            heapq.heapify(sublist)

        # can try a combo for each vertex
        max_val = float("-inf")

        for i, sublist in enumerate(neighbors):
            curr = vals[i] 
            for i in range(k):
                if sublist:
                    to_add = heapq.heappop(sublist)
                    if to_add >= 0:
                        break
                    curr -= to_add
                else:
                    break
            

            max_val = max(max_val, curr)
        
        return max_val if max_val != float("-inf") else 0

# TC : O(E + k * V)
# SC : O(E)
