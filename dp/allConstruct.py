"""
return list of all possible combination
"""

def allConstruct(words, target):
    if target == '':
        return [[]]
    result= []
    for word in words:
        if target.startswith(word):
            suffix=target[len(word):]
            suffixways = allConstruct(words, suffix)
            targetways = list(map(lambda way:[word, *way], suffixways))
            result.extend(targetways)
    return result

def allConstructMemo(words, target, memo):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result= []
    for word in words:
        if target.startswith(word):
            suffix=target[len(word):]
            suffixways = allConstructMemo(words, suffix, memo)
            targetways = list(map(lambda way:[word, *way], suffixways))
            result.extend(targetways)
    memo[target]= result
    return result

def allConstructTab(words, target):
    # special case of 2d array python to avoid multiple copying of element
    table = ['']*(len(target)+1)
    table = list(map(lambda x: [],table ))
    table[0]=[[]]
    for i in range(len(target)+1):
        if table[i]==[]:
            continue
        for word in words:
            if target[i:len(word)+i]==word:
                newtable= list(map(lambda subarray: [*subarray, word], table[i]))
                table[i+len(word)].extend(newtable)
    return table[len(target)]

if __name__ == "__main__":
    words = ["purp",'p','ur', 'le', "purpl"]
    target = "purple"
    print(allConstruct(words, target))
    print(allConstructMemo(words, target, dict()))
    print(allConstructTab(words, target))
    words = ['ab','abc','cd','def','abcd','ef','c']
    target = "abcdef"
    print(allConstruct(words, target))
    print(allConstructMemo(words, target, dict()))
    print(allConstructTab(words, target))