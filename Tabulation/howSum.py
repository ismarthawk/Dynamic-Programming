def howSum(target, nums) :
    dp = [None for i in range(target + 1)]
    dp[0] =  []
    for i in range(target) :
        if dp[i] is not None :
            for num in nums :
                sm = i + num
                if sm <= target :
                    dp[sm] = dp[i] + [num]
    return dp[target]

print(howSum(2250, [4,2,3]))
