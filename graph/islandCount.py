def islandcount(grid)->int:
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count+=1
    return count

def explore(grid, r, c, visited):
    rowinbound = 0<=r and r<len(grid)
    colinbound = 0<=c and c<len(grid[0])
    if not rowinbound or not colinbound:
        return False
    if grid[r][c]=='w':
        return False
    pos = str(r)+','+str(c)
    if pos in visited:
        return False
    visited.add(pos)
    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c+1, visited)
    explore(grid, r, c-1, visited)
    return True

if __name__ == "__main__":
    grid = [
        ['w','l','w','w','w'],
        ['w','l','w','w','w'],
        ['w','w','w','l','w'],
        ['w','w','l','l','w'],
        ['l','w','w','l','l'],
        ['l','l','w','w','w'],
    ]
    print(islandcount(grid))