memo = dict()
memo[0] = []

def howSum(nums, target, memo) :
    if target < 0 : return None
    if target in memo : return memo[target]
    for num in nums :
        newTarget = target - num
        if howSum(nums, newTarget, memo) is not None :
             memo[target] = howSum(nums, newTarget, memo) + [num]
             return memo[target]
    memo[target] = None
    return None

print(howSum([4,2,3], 2225, memo))
