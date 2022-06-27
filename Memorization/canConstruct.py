
def canConstructRec(target, bank) :
    if target == '' : return True
    if target in bank : return True
    curr = ''
    for i in range(len(target)) :
        curr += target[i]
        if curr in bank :
            if canConstructRec(target[i+1:], bank) :
                return True
    return False

def canConstruct(target, bank, memo = {}) :
    if target == '' : return True
    if target in bank : return True
    if target in memo : return memo[target]
    curr = ''
    memo[target] = False
    for i in range(len(target)) :
        curr += target[i]
        if curr in bank :
            if canConstruct(target[i+1 : ], bank, memo) :
                memo[target] = True
                return True
    return memo[target]


print(canConstruct('abcd', {'ab', 'bc','cde', 'f', 'abacd'}))
