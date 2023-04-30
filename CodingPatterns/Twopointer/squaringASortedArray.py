def sortedSquares(A):
    l, r, answer = 0, len(A) - 1, [0] * len(A)
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        answer[r - l] = max(left, right) ** 2
        l, r = l + (left > right), r - (left <= right)
    return answer

if __name__ == '__main__':
    A= [-7,-3,2,3,11]
    print(sortedSquares(A))