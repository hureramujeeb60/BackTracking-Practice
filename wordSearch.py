from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
    
        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >=cols or word[i] != board[r][c] or board[r][c] == '#':
                return False
            
            board[r][c] = '#'
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            board[r][c] = word[i]
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
            
        return False


if __name__ == "__main__":
    board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    sol = Solution()
    result = sol.exist(board,word)
    print(result)