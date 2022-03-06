class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.BOARD= board
        self.ROWS = len(board)
        self.COLS = len(board[0])
        
        
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
    def backtrack(self, row, col, s):
            if len(s) == 0:
                return True
                
            if row < 0 or row== self.ROWS or col == self.COLS or col<0 or self.BOARD[row][col] != s[0]:
                return False
            
            isSol = False
        
            self.BOARD[row][col] = '#'
            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                isSol = self.backtrack(row + rowOffset, col + colOffset, s[1:]) 
                if isSol: break

            # revert the change, a clean slate and no side-effect
            self.BOARD[row][col] = s[0]

            # Tried all directions, and did not find any match
            return isSol
            