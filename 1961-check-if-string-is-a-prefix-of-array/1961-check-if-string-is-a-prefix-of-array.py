class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:        
        result=False
        join=""
        for i in words:
            join+=i
            if s.startswith(join) and len(join)<len(s):
                continue
            elif s.startswith(join) and len(join)==len(s):
                result=True
                break
            else:
                result=False
                break
        return result