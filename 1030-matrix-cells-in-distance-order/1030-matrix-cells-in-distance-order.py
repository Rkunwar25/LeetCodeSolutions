class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        cells = []

        for r in range(rows):
            for c in range(cols):
                cells.append([r, c])

        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return cells
