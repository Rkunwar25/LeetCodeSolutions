# class Solution:
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         allowed=list(allowed)
#         count=0
#         for i in words :
#             if set(list(i)).issubset(set(allowed)): 
#                 count+=1
#         return count
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(set(word).issubset(allowed) for word in words)
