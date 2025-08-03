class Solution(object):
    def findRestaurant(self, list1, list2):
        l=list(set(list1).intersection(set(list2)))
        if len(l)==1:
            return l
        l1=dict()
        for i in l:
            l1[i]=list1.index(i)+list2.index(i)
        vals=[]
        for i in l1.values():
            vals.append(i)
        v=min(vals)
        ans=[]
        for i in l1:
            if l1[i]==v:
                ans.append(i)
        return ans