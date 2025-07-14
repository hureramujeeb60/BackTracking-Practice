class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        cols = len(maze[0])
        dir_row = [1,0,0,-1]
        dir_col = [0,-1,1,0]
        dir_str = "DLRU"
        all_path = []
        path = ""
        
        def dfs(r, c,path):
            if r == n-1 and c == cols-1:
                all_path.append(path)
                return
            
            maze[r][c] = 0
 
            for i in range(4):
                new_row = r + dir_row[i]
                new_col = c + dir_col[i]
                if self.isValid(new_row, new_col, maze, n, cols):
                    dfs(new_row, new_col, path + dir_str[i])

            maze[r][c] = 1
            
        if maze[0][0] == 1:
            dfs(0,0,path)
        return all_path
                
    def isValid(self,r, c, maze, n,cols):
        return 0 <= r < n and 0 <= c < cols and maze[r][c] == 1

if __name__ == "__main__":
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    sol = Solution()
    print(sol.ratInMaze(maze))