class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        if start not in visited:
            print(start, end=' ')
            visited.add(start)
            for neighbor in self.graph[start]:
                self.dfs(neighbor, visited)

if __name__ == "__main__":
    # Example usage:
    graph = Graph()

    # Adding edges to the graph
    graph.add_edge(0, [1, 2])
    graph.add_edge(1, [2])
    graph.add_edge(2, [0, 3])
    graph.add_edge(3, [3])

    print("DFS starting from node 2:")
    graph.dfs(2)
