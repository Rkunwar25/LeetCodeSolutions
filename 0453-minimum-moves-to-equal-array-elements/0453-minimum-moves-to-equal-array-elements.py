class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mn = min(nums)
        moves = 0
        
        for num in nums:
            moves += num - mn
            
        return moves
