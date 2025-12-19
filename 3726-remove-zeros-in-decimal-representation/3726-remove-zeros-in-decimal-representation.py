class Solution:
    def removeZeros(self, n: int) -> int:
        n=str(n)
        if "0" not in n:
            return int(n)
        n=list(n)
        n=[i for i in n if i!="0"]
        return int("".join(n))