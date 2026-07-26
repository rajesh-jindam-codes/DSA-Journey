from collections import deque
board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
class Solution:
    def solve(self,board):
        rows=len(board)
        cols=len(board)
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if (r==0 or c==0 or r>=rows-1 or c>=cols-1) and board[r][c]=='O':
                    queue.append([r,c])
                    board[r][c]='S'
        while len(queue)!=0:
            i,j=queue.popleft()
            for dx,dy in [(-1,0),(0,1),(0,-1),(1,0)]:
                newI,newJ=i+dx,j+dy
                if newI<0 or newJ<0 or newI>=rows or newJ>=cols:
                    continue
                if board[newI][newJ]!='O':
                    continue
                board[newJ][newJ]='S'
                queue.append([newI,newJ])
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='S':
                    board[r][c]='O'
        return board
obj=Solution()
print(obj.solve(board))