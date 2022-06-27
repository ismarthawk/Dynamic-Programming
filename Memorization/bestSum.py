

def bestSum(nums, target, memo = dict()) :
    if target < 0 : return None
    if target == 0 : return []
    if target in memo : return memo[target]
    memo[target] = None
    for num in nums :
        newTarget = target - num
        res = bestSum(nums, newTarget, memo)
        if res is not None :
            if not memo[target] :
                memo[target] = res + [num]
            else :
                memo[target] = res + [num] if len(res) <= len(memo[target]) else  memo[target]
    return memo[target]


nums = [3, 5, 8, 9]
target = 13
print(bestSum(nums, target))
