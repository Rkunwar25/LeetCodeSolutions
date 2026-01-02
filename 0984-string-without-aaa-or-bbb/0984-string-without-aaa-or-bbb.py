class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        
        while a > 0 or b > 0:
            # If last two are 'a', must place 'b'
            if len(res) >= 2 and res[-1] == res[-2] == 'a':
                res.append('b')
                b -= 1
            
            # If last two are 'b', must place 'a'
            elif len(res) >= 2 and res[-1] == res[-2] == 'b':
                res.append('a')
                a -= 1
            
            # Otherwise, place the character with higher remaining count
            elif a >= b and a > 0:
                res.append('a')
                a -= 1
            else:
                res.append('b')
                b -= 1
        
        return "".join(res)
