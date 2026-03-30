class Solution:
    def distanceToOrigin(self, point: List[int]) -> float:
        return math.sqrt(point[0]**2 + point[1]**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = []
        heap = []

        for point in points:
            # Negative distance to maintain max_heap
            negative_dist = -self.distanceToOrigin(point)
            if len(heap) == k and -heap[0][0] > -negative_dist:
                heapq.heappop(heap) # eliminate curr_max if next distance is smaller
            
            # Always populate until reach k
            if len(heap) < k:
                heapq.heappush(heap, (negative_dist, point))
        
        for _ in range(k):
            results.append(heapq.heappop(heap)[1])

        return results