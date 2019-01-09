class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        N = len(grid)
        M = len(grid[0])
        rows_max = [0] * N
        cols_max = [0] * M
        for i in xrange(N):
            for j in xrange(M):
                cell_val = grid[i][j]
                cols_max[j] = max(cell_val, cols_max[j])
                rows_max[i] = max(cell_val, rows_max[i])
        running_sum = 0
        for i in xrange(N):
            for j in xrange(M):
                cell_val = grid[i][j]
                min_height = min(cols_max[j], rows_max[i])
                running_sum += min_height - cell_val
        return running_sum