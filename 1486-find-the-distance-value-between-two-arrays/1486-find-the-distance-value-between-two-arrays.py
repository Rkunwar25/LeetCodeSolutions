class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        c=0
        for i in arr1:
            flag=0
            for j in arr2:
                if abs(i-j)<=d:
                    flag=1
                    break
            if flag==0:
                c+=1
        return c