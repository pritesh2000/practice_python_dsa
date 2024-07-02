points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

distances = min(points)
print(distances)

print(points)
dictionary = {}

for x, y in points:
    # print(x,y, 'outer')
    minimum = float("inf")
    for x1, y1 in points:
        if x == x1 and y == y1 or abs(x-x1) + abs(y-y1) > minimum:
            pass
        else:
            # print(x1,y1, "inner") 
            minimum = abs(x-x1) + abs(y-y1)
    print(minimum)
    dictionary[x,y] = minimum

print(dictionary)

# same problem with new solution
N = len(points)
adj = {i:[] for i in range(N)}

for i in range(N):              # very good logic
    x2,y2 = points[i]
    for j in range(i+1,N):
        x3,y3 = points[j]
        dist = abs(x3-x2) + abs(y3-y2)
        adj[i].append([dist, j])
        adj[j].append([dist, i])

print(adj)







