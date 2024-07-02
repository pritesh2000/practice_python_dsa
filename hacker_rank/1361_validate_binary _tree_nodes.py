def dfs(node):
    if node in visited:
        return False
    ans = True
    visited.append(node)
    print('be for ', node)
    for i in graph[node]:
        print(i, graph[node])
        ans = ans and dfs(i)
    print('end for')
    return ans

from collections import defaultdict
graph = defaultdict(list)
print(type(graph))
graph[0] = [1,2]
graph[2] = [3]
print(type(graph))
print(graph)
visited = []
ans = dfs(0)
print(ans)

for i in graph.keys():
    c = i
    print(i)
print(c)