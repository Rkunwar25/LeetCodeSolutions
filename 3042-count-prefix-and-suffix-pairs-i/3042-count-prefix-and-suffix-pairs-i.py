class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def  isPrefixAndSuffix(str1,str2):
            if str1 not in str2:
                            return False 
            return True if str2.startswith(str1) and str2.endswith(str1) else False
        count=0
        n=len(words)
        for i in range(n-1):
            for j in range(i+1,n):
                if isPrefixAndSuffix(words[i],words[j]):
                    count+=1
        return count 