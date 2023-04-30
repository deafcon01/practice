def spiralOrder(mat: list[list[int]])-> list[int]:
    #base
    if not mat or not len(mat):
        return mat
    top,left=0,0
    bottom,right=len(mat)-1, len(mat[0])-1
    ans=list()
    while 1:
        if left> right:
            break
        for i in range(left, right+1):
            ans.append(mat[top][i])
        top+=1
        if top> bottom:
            break
        for i in range(top, bottom+1):
            ans.append(mat[i][right])
        right-=1
        if left>right:
            break
        for i in range(right, left-1,-1):
            ans.append(mat[bottom][i])
        bottom-=1
        if top>bottom:
            break
        for i in range(bottom, top-1, -1):
            ans.append(mat[i][left])
        left+=1
    return ans

if __name__ == '__main__':
 
    # mat = [
    #     [1, 2, 3, 4, 5],
    #     [16, 17, 18, 19, 6],
    #     [15, 24, 25, 20, 7],
    #     [14, 23, 22, 21, 8],
    #     [13, 12, 11, 10, 9]
    # ]
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder(mat))
