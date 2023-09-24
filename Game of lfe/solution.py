import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        boardCopy=board.copy()

        def countNeighbor(x,y):
            kernal= [[x-1,y-1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1],[x-1,y]]
            count=0
            for i,j in kernal:
                if (-1<i<m) and (-1<j<n):
                    count+=boardCopy[i][j]
            return count
            
        boardCopy=copy.deepcopy(board)

        for i in range(m):
            for j in range(n):
                count=countNeighbor(i,j) 
                if boardCopy[i][j]==1 and count<2 or count>3: 
                    board[i][j]=0 
                if boardCopy[i][j]==0 and count==3: 
                    board[i][j]=1
