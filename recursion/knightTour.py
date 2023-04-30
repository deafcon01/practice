pathrow = [2,1,-1,-2,-2,-1,1,2]
pathcol = [1,2,2,1,-1,-2,-2,-1]

def knighttour(visited, row, col, move):
    if move==64:
        for i in range(8):
            for j in range(8):
                print(visited[i][j], end='\t')
            print()
        return True
    for idx in range(len(pathrow)):
        rownew = row + pathrow[idx]
        colnew = col + pathcol[idx]
        if validmove(visited, rownew, colnew):
            move+=1
            visited[rownew][colnew]=move
            if knighttour(visited, rownew, colnew, move):
                return True
            move-=1
            visited[rownew][colnew]=0
    return False

def validmove(visited, r, c):
    if r>=0 and r<8 and c>=0 and c<8 and visited[r][c]==0:
        return True
    return False


if __name__ == '__main__':
    visited = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    visited[0][0] = 1
    knighttour(visited, 0,0,1)