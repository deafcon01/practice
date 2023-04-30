def minIsland(grid):
    visited= set()
    minisland= float('inf')
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size =  exploreSize(grid, r, c, visited)
            if size>0:
                minisland =  min (minisland, size)
    return minisland


def exploreSize(grid, r, c, visited):
    rowinbounds = 0<= r and r< len(grid)
    colinbounds = 0<= c and c<len(grid[0])
    if not rowinbounds or not colinbounds:
        return 0
    if grid[r][c]=='w':
        return 0
    pos= str(r)+","+str(c)
    if pos in visited:
        return 0
    visited.add(pos)
    size =1
    size+=exploreSize(grid, r-1, c , visited)
    size+=exploreSize(grid, r+1, c , visited)
    size+=exploreSize(grid, r, c-1 , visited)
    size+=exploreSize(grid, r, c+1 , visited)
    return size

if __name__ == "__main__":
    grid = [
        ['w','l','w','w','w'],
        ['w','l','w','w','w'],
        ['w','w','w','l','w'],
        ['w','w','l','l','w'],
        ['l','w','w','l','l'],
        ['l','l','w','w','w'],
    ]
    print(minIsland(grid))