n = 2
m = 3
k = 1

n = 4
m = 5
k = 3

dp = [[[0] * (k+1) for _ in range(m+1)]for _ in range(n+1)]

dp[0][0][0] = 1

for i in range(1,n+1):
    print(i, '---------------')
    for j in range(1,m+1):
        print(j, 'loop')
        for cost in range(1,k+1):
            dp[i][j][cost] += dp[i-1][j][cost] *j
            for pre in range(j):
                dp[i][j][cost] += dp[i-1][pre][cost-1]
            print(i,j,cost, 'dp', dp[i][j][cost])
        print()
    print()

print(dp)
a = sum(dp[n][i][k] for i in range(1,m+1))
print(a)

for i in range(n+1):
    print(i,'-------------------')
    for j in range(m+1):
        for c in range(k+1):
            print(dp[i][j][c], end=" ")
        print()
    print()