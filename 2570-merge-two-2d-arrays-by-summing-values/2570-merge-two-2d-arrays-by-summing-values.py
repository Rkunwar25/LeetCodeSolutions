class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d1=dict()
        d2=dict()
        s=set()
        for i in nums1:
            d1[i[0]]=i[1]
            s.add(i[0])
        for i in nums2:
            d2[i[0]]=i[1]
            s.add(i[0])
        s=sorted(list(s))
        ans=[]
        for i in s:
            if i in d1 and i in d2:
                ans.append([i,d1[i]+d2[i]])
            elif i in d1 and i not in d2:
                ans.append([i,d1[i]])
            elif i in d2 and i not in d1:
                ans.append([i,d2[i]])
        return ans