class Solution(object):
    def decode(self, encoded, first):
        arr = [first]
        
        for e in encoded:
            arr.append(arr[-1] ^ e)
        
        return arr
