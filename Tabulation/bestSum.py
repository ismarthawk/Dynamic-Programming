def bestSum(target, nums) :
    dp = [None for i in range(target + 1)]
    dp[0] = []
    for i in range(target) :
        if dp[i] is not None :
            for num in nums :
                sm = i + num
                if sm <= target and dp[sm] is None :
                    dp[sm] = dp[i] + [num]
                else :
                    if sm <= target and len(dp[i]) < len(dp[sm]) :
                        dp[sm] = dp[i] + [num]
    return dp[target]

nums = [3, 5, 8, 9]
target = 13
print(bestSum(target, nums))
