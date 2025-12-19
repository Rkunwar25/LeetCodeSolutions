# class Solution:
#     def gcdOfOddEvenSums(self, n: int) -> int:
#         def gcd(a,b):
#             while b:
#                 a,b=b,a%b
#             return abs(a)
#         odd=even=0
#         for i in range(1,n+1):
#             odd+=(2*i)-1
#             even+=2*i
#         return gcd(odd,even)
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
