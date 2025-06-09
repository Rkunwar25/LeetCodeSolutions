class Solution(object):
    def nextGreaterElement(self, n):
        MAX_INT = 2**31 - 1
        p=permutations(str(n))
        result=[]
        for i in p:
            val = int(''.join(i))
            if val <= MAX_INT:
                result.append(val)
        result=list(set(result))
        result.sort()        
        if max(result)!=n:
            return result[result.index(n)+1]
        return -1