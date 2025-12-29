class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()   # ensures shortest root is checked first
        words = sentence.split()
        
        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break
        
        return " ".join(words)
