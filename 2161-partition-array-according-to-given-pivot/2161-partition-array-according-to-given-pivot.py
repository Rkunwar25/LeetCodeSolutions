class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        g=[]
        c=0
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i>pivot:
                g.append(i)
            else:
                c+=1
        l.extend([pivot]*c)
        l.extend(g)
        return l