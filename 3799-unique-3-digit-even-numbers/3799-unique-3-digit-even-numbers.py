from itertools import permutations

class Solution(object):
    def totalNumbers(self, digits):
        seen = set()        
        for p in permutations(digits, 3):
            if p[0] == 0:
                continue  
            if p[2] % 2 != 0:
                continue  
            number = p[0] * 100 + p[1] * 10 + p[2]
            seen.add(number)
        return len(seen)