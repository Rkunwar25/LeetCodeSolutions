class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=list(allowed)
        count=0
        for i in words :
            if set(list(i)).issubset(set(allowed)): 
                count+=1
        return count