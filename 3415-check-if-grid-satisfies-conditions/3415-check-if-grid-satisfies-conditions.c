#include <stdbool.h>

bool satisfiesConditions(int** grid, int gridSize, int* gridColSize) {
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            // Check cell below (if it exists)
            if (i + 1 < gridSize && grid[i][j] != grid[i + 1][j]) {
                return false;
            }
            // Check cell to the right (if it exists)
            if (j + 1 < gridColSize[i] && grid[i][j] == grid[i][j + 1]) {
                return false;
            }
        }
    }
    return true;
}
