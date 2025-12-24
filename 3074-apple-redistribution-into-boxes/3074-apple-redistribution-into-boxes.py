class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple.sort(reverse=True)
        capacity.sort(reverse=True)
        n=len(capacity)
        s=sum(apple)
        c=0
        count=0
        for i in range(n):
            if capacity[i]+c<s:
                c+=capacity[i]
                count+=1
            elif c+capacity[i]>=s:
                count+=1
                break
        return count        