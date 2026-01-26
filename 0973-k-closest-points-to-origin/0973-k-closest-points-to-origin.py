class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for point in points:
            dist.append(math.sqrt(point[0]**2+point[1]**2))
        c=0
        ans=[]
        while c<k:
            mn=dist.index(min(dist))
            ans.append(points[mn])
            dist[mn]=float('inf')
            c+=1
        return ans