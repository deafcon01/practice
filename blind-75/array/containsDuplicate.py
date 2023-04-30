def duplicate():
    nums = [1, 5, 2, 4, 1]
    visited = set()
    dup = {x for x in nums if x in visited or (visited.add(x))}
    if len(dup) == 0:
        return True
    return False
print(duplicate())