def hasDup(s,k)->bool:
    w={}
    for i,e in enumerate(s):
        if e in w:
            if i-w.get(e)<=k:
                return True
        w[e]=i
    return False

if __name__ == '__main__':
 
    nums = [5, 6, 8, 2, 4, 6, 9]
    k = 4
 
    if hasDup(nums, k):
        print('Duplicates found')
    else:
        print('No duplicates were found')