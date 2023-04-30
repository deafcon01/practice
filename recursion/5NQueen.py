"""
Given a board place queens on each row such that they dont attack each other.
"""
def validCell( board, newrow, newcol, size):
    """
    Need to check uuper half for straight and diagonals
    """
    for i in range(size):
        if board[i][newcol]:
            return False
    for i,j in zip(range(newrow,-1,-1), range(newcol,-1,-1)):
        if board[i][j]:
            return False
    for i,j in zip(range(newrow, -1, -1), range(newcol, size, 1)):
        if board[i][j]:
            return False
    return True

def NQueen(board, size:int, row:int):
    if row==size-1:
        for i in range(size):
            for j in range(size):
                print( board[i][j], end="\t")
            print()
        return True
    for col in range(size):
        newrow=row+1
        if validCell(board, newrow, col, size):
            board[newrow][col]=True
            if NQueen(board, size, newrow):
                return True
            board[newrow][col]=False
    return False

if __name__ == "__main__":
    board = [
        [False, False, False,False,False, False, False,False],
        [False, False, False,False,False, False, False,False],
        [False, False, False,False,False, False, False,False],
        [False, False, False,False,False, False, False,False],
        [False, False, False,False,False, False, False,False],
        [False, False, False,False,False, False, False,False],
        [False, False, False,False,False, False, False,False],
        [False, False, False,False,False, False, False,False],
    ]
    print(NQueen(board, 8, -1))