from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        n = len(grid)
        dir_row = [-2, -1, 1, 2, 2, 1, -1, -2]
        dir_col = [1, 2, 2, 1, -1, -2, -2, -1]

        def backtrack(r, c, moves):
            if moves == (n*n)-1:
                return True
            
            
            for i in range(8):
                
                new_row = r + dir_row[i]
                new_col = c + dir_col[i]

                if self.isValid(new_row, new_col, grid, moves+1):
                    if backtrack(new_row, new_col, moves+1):
                        return True
            return False
        return backtrack(0,0,0)
    def isValid(self, r, c, grid, moves):
        return 0 <= r < len(grid) and 0 <= c < len(grid) and grid[r][c] == moves

if __name__ == "__main__":
    grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
    sol = Solution()
    print(sol.checkValidGrid(grid))