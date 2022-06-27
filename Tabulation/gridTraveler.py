def gridTraveler(rows, cols) :
    dp = [[0 for i in range(cols+1)] for k in range(rows+ 1)]
    for i in range(1, rows + 1) :
        for j in range(1, cols + 1) :
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            if i == 1 and j == 1 : dp[1][1] = 1
    return dp[rows][cols]

print(gridTraveler(3, 3))
