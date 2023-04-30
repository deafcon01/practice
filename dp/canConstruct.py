"""
possiblity to generate target word from list of words
"""
def canConstruct(words, target):
    if target == "":
        return True
    
    for word in words:
        if target.startswith(word):
            suffix=target[len(word):]
            if canConstruct(words, suffix)==True:
                return True
    return False

def canConstructMemo(words, target, memo):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    
    for word in words:
        if target.startswith(word):
            suffix=target[len(word):]
            if canConstructMemo(words, suffix, memo)==True:
                memo[target] = True
                return True
    memo[target] = False
    return False

def canConstructTab(words, target):
    table = [False]*(len(target)+1)
    table[0]=True
    for i in range(len(target)+1):
        if table[i] == False:
            continue
        for word in words:
            if (i+len(word))<=len(target) and target[i:len(word)+i]==word:
                table[i+len(word)]=True
    return table[len(target)]

if __name__ == '__main__':
    words=['ab', 'abc', 'cd', 'def', "abcd"]
    target= "abcdef"
    # print(canConstruct(words, target))
    print(canConstructMemo(words, target, dict()))
    print(canConstructTab(words, target))