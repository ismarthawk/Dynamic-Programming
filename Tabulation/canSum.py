def canSum(target, nums) :
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for i in range(target + 1) :
        if dp[i] :
            for num in nums :
                if i + num <= target : dp[i + num] = True
    # print(dp)
    return dp[target]

arr = [8, 5]
target = 14

print(canSum( target, arr))
