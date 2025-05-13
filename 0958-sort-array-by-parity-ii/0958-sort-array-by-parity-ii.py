class Solution(object):
    def sortArrayByParityII(self, nums):
        odd=[]
        even=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        l=[]
        c=0
        while c<len(odd) and c<len(even) :
            l.append(even[c])
            l.append(odd[c])
            c+=1
        return l