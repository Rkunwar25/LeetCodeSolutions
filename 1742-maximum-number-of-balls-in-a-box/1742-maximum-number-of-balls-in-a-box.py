class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            box[sum(map(int,list(str(i))))]+=1
        return max(box.values())