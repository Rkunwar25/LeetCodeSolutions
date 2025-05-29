class Solution(object):
    def canAliceWin(self, n):
        turn = 0  # 0 = Alice, 1 = Bob
        remove = 10
    
        while n >= remove:
           n -= remove
           remove -= 1
           turn ^= 1
        return turn == 1 