class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=[]
        for i in range(1,len(num)-1):
            if num[i-1]==num[i]==num[i+1]:
                l.append(num[i]*3)
        if not l:
            return ""
        else: 
            return max(l)