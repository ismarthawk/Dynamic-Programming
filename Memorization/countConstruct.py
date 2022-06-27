from collections import defaultdict

def countConstruct(target, bank, memo = defaultdict(lambda : 0)) :
    if target == '' : return 1
    if target in memo : return memo[target]
    curr = ''
    for i in range(len(target)) :
        curr += target[i]
        if curr in bank :
            memo[target] += countConstruct(target[i+1 : ], bank, memo)
    return memo[target]

print(countConstruct('purple', {'pu','rp','l', 'e','pur', 'p', 'le'}))
