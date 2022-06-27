memo = {}

def canSumRec(nums, target) :
    if target == 0 : return True
    if target < 0 : return False
    for num in nums :
        if canSum(nums, target - num) :
            return True
    return False


def canSum(nums, target, memo) :
    if target == 0 : return True
    if target < 0 : return False
    if target in memo : return memo[target]
    for num in nums :
        if canSum(nums, target - num, memo) :
            memo[target] = True
            return True
    memo[target] = False
    return False

arr = [3, 5]
target = 12

print(canSum(arr, target, memo))
