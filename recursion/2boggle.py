"""
Given a dictionary, a method to do lookup in dictionary and a MxN board where
every cell has one character. Find all possible work that can be formed by a 
sequence of adjacent charcaters. 
word should not have multiple instance of same cell.
"""
pathrow = [0,0,1,1,-1,1,-1,-1]
pathcol = [1,-1,-1,1,1,0,0,-1]
def boggle(board, visited, row, col, word, dictionary):
    if word in dictionary:
        print(word)
    if len(word)==len(board)*len(board[0]):
        return
    for i in range(len(pathrow)):
        newrow=row+pathrow[i]
        newcol=col+pathcol[i]
        rowinbounds= 0<=newrow and newrow<len(board)
        colinbounds = 0<=newcol and newcol<len(board[0])
        if (rowinbounds and colinbounds and visited[newrow][newcol]==False):
            visited[newrow][newcol]=True
            boggle(board,visited, newrow, newcol, word+board[newrow][newcol], dictionary)
            visited[newrow][newcol]=False
        


if __name__ ==  '__main__':
    board = [
        ['g','i','z'],
        ['u','e','k'],
        ['q','s','e'],
        ]
    dictionary = ['geeks', 'quiz', 'for', 'go', 'see']
    visited = [
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]
    word=''
    for r in range(len(board)):
        for c in range(len(board[0])):
            visited[r][c] = True
            boggle(board, visited, 0,0, word+board[r][c], dictionary)
            visited[r][c] = False