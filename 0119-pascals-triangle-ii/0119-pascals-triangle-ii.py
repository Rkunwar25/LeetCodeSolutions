class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            row[i] = row[i - 1] * (rowIndex - i + 1) // i

        return row
