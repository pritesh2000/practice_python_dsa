import collections
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

adjacency = collections.defaultdict(list)
print(adjacency)

for u, v in tickets:
    adjacency[u].append(v)
print(adjacency)

for key in adjacency:
    adjacency[key].sort()
print(adjacency.keys())
print(adjacency.values())

curr = ["JFK"]
output = []

while curr:
    dec = curr[-1]
    
    if adjacency[dec] == []:
        output.append(dec)
        curr.pop()

    else:
        curr.append(adjacency[dec].pop(0))

print(output[::-1])
        
        