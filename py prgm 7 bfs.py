from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            current_node = queue.popleft()

            if current_node not in visited:
                print(current_node, end=' ')
                visited.add(current_node)
                queue.extend(neighbor for neighbor in self.graph[current_node] if neighbor not in visited)

if __name__ == "__main__":
    # Example usage:
    graph = Graph()

    # Adding edges to the graph
    graph.add_edge(0, [1, 2])
    graph.add_edge(1, [2])
    graph.add_edge(2, [0, 3])
    graph.add_edge(3, [3])

    print("BFS starting from node 2:")
    graph.bfs(2)
