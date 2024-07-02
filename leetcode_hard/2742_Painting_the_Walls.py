cost = [1,2,3,2]
time = [1,2,3,2]

cost = [2,3,4,2]
time = [1,1,1,1]

n = len(time)

money = [float('inf')] * (n+1)
money[0] = 0
for i in range(n):
    for j in range(n,0,-1):
        print(i,j)
        money[j] = min(money[j], money[max(j-time[i]-1, 0)]+ cost[i])
        print(money)
# print(money)