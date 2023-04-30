"""
Count number of ways a word can be constructed
"""
def countConstruct(words, target):
    if target == "":
        return 1
    total =0
    for word in words:
        if target.startswith(word):
            suffix=target[len(word):]
            numways = countConstruct(words, suffix)
            total+=numways   
    return total

def countConstructMemo(words, target, memo):
    if target in memo:
        return target
    if target == "":
        return 1
    total =0
    for word in words:
        if target.startswith(word):
            suffix=target[len(word):]
            numways = countConstruct(words, suffix)
            total+=numways
    memo[target]=total   
    return total

def countConstructTab(words, target):
    table = [0]*(len(target)+1)
    table[0]=1
    for i in range(len(target)+1):
        if table[i] == 0:
            continue
        for word in words:
            if (i+len(word))<=len(target) and target[i:len(word)+i]==word:
                table[i+len(word)]+=table[i]
    return table[len(target)]

if __name__ == "__main__":
    words = ["purp",'p','ur', 'le', "purpl"]
    target = "purple"
    print(countConstruct(words, target))
    print(countConstructMemo(words, target, dict()))
    print(countConstructTab(words, target))