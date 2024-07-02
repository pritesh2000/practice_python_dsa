import heapq
heights = [[1,2,2],[3,8,2],[5,3,5]]

m, n = len(heights), len(heights[0])

dist = [[float("inf") for j in range(n)]for i in range(m)]
dist[0][0] = 0

pq = [(0,0,0)]

while pq:
    min_avg_cost, i, j= heapq.heappop(pq)

    if i == m-1 and j == n-1:
        break

    for x,y  in [(i-1,j),(i+1,j), (i,j-1),(i,j+1)]:
        if 0 <= x < m and 0 <= y < n:
            t = max(abs(heights[i][j]-heights[x][y]), min_avg_cost)
            if dist[x][y] > t:
                dist[x][y] = t
                heapq.heappush(pq, (dist[x][y],x,y))

print(min_avg_cost)
print(t)
for i in dist:
    print(i)