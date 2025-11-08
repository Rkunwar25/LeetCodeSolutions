class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        d=1
        num=0
        for i in digits:
            num+=i*d
            d*=10
        num+=1
        return list(map(int,list(str(num))))