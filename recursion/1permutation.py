"""
Print all permutation of the string.
"""
def permutation(input:list, result:list, count:list, level:int):
    """
    level: result list index position
    count: to check if char is visited
    result: to print permutation
    input: input list
    """
    if level== len(input):
        print(result)
    for i in range(len(input)):
        if count[i]==0:
            continue
        result[level]=input[i]
        count[i]-=1
        permutation(input, result, count, level+1)
        count[i]+=1
    
if __name__ == '__main__':
    permutation(['a','b','c','d'],[None, None, None, None], [1,1,1,1], 0)