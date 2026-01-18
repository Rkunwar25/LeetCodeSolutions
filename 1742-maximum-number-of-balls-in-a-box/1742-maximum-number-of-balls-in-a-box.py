class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            s=list(str(i))
            s1=sum(map(int,s))
            box[s1]+=1
        # print(box)
        return max(box.values())