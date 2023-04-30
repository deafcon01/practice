pathrow = [0,0,1,-1]
pathcol = [1,-1,0,0]
def ratmaze(maze:list[list[int]], visited, row, col, destrow, destcol, move):
    if row==destrow and col==destcol:
        for i in range(4):
            for j in range(4):
                print(visited[i][j], end='\t')
            print()
        print("---")
    else:
        for idx in range(len(pathrow)):
            rownew= row+pathrow[idx]
            colnew= col+pathcol[idx]
            if validmove(rownew, colnew, visited, maze):
                move+=1
                visited[rownew][colnew]=move
                ratmaze(maze, visited, rownew, colnew, destrow, destcol, move)
                move-=1
                visited[rownew][colnew]=0

def validmove(r, c, visited, maze):
    if r>=0 and r<4 and c>=0 and c<4 and maze[r][c]==1 and visited[r][c]==0:
        return True
    return False

if __name__=='__main__':
    maze= [
        [1,1,0,1],
        [0,1,1,1],
        [0,1,0,1],
        [0,1,1,1]
    ]
    visited = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    visited[0][0]=1
    ratmaze(maze, visited, 0,0,3,3,1)