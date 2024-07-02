from collections import defaultdict, deque

# getting topological order Kahn's Algorithms

class Graph:

    def __init__(self, n) -> None:
        self.num_vertices = n
        self.indegree = defaultdict(lambda : 0)
        self.neighbours = defaultdict(list)

    def addEdge(self, u, v):
        self.neighbours[u].append(v)
        self.indegree[v] += 1

    def printer(self):
        print(self.neighbours)
        print(self.indegree)

    def kahnsAlgo(self, n):
        
        final = deque()
        topological_order = []

        for i in range(1, n+1):
            if self.indegree[i] == 0:
                final.append(i)
        print(final, 'prior to while')
        
        while final:
            u = final.popleft()
            topological_order.append(u)
            for v in self.neighbours[u]:
                self.indegree[v] -= 1
                if self.indegree[v] == 0:
                    final.append(v)
        
        print(final, 'after while')

        if len(topological_order) != n:
            topological_order = []
            
        print(topological_order)
        return topological_order




graph = Graph(5)
print(graph)

vertices = [[1,5],[2,5],[3,5],[3,4],[4,5]]

for i in vertices:
    graph.addEdge(i[0], i[1])

print(graph)
graph.printer()
graph.kahnsAlgo(5)