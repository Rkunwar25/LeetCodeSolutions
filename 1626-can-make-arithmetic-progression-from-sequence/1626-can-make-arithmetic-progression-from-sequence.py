class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        l1=sorted(arr)
        # l2=sorted(arr,reverse=True)
        cd1=l1[1]-l1[0]
        # cd2=l2[1]-l2[0]
        flag=True
        for i in range(2,len(l1)):
            if l1[i]-l1[i-1]!=cd1:
                flag=False
                break
        return flag
        