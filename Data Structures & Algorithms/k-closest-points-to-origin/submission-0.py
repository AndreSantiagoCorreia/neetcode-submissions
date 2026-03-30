class Solution:
    def distanceToOrigin(self, point: List[int]) -> float:
        return math.sqrt(point[0]**2 + point[1]**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = []
        heap = []

        for point in points:
            dist = self.distanceToOrigin(point)
            heapq.heappush(heap, (dist, point))
        
        for _ in range(k):
            results.append(heapq.heappop(heap)[1])

        return results