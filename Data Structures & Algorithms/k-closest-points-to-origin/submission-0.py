from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        # push in the distance along with the points
        for i in points:
            x, y = i[0], i[1]
            distance = sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (distance, [x, y]))

        for i in range(k):
            dist, coordinates = heapq.heappop(minHeap)
            res.append(coordinates)
        
        return res