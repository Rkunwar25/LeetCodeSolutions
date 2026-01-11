class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        # Step 1: Find the block
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # Step 2: Find the number
        num = start + (n - 1) // length

        # Step 3: Find the digit
        return int(str(num)[(n - 1) % length])
