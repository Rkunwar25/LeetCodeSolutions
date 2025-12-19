import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digSum=sum(map(int,str(n)))
        digProd=math.prod(map(int, str(n)))
        return n%(digSum+digProd)==0