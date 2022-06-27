from collections import defaultdict
memo = defaultdict(lambda : [])
def allConstruct(target, bank) :
    if target == '' : return [[]]
    if target in memo : return memo[target]
    curr = ''
    d = dict()
    for i in range(len(target)) :
        curr += target[i]
        newTarget = target[i+ 1 : ]
        if curr in bank :
            res = allConstruct(newTarget, bank)
            if len(res) > 0 :
                d[curr] = res
    for pre in d :
        for li in d[pre] :
            memo[target].append([pre] + li)
    return memo[target]







print(allConstruct('purple', {'pu','rp','l', 'e','pur', 'p', 'le'}))
print(allConstruct('abcdef', {'ab','abc','cd', 'def','abcd', 'ef', 'c'}))
