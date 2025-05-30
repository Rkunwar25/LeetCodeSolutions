int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int c=0;
    int i,j;
    for (i=0;i<gridSize;i++)
    {
        for (j=0;j<*gridColSize;j++)
        {
            if(grid[i][j]<0)
              c++;
        }
    }
    return c;
}