import heapq

class Node:
    def __init__(self, x, y, cost, heuristic):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != 1

    def calculate_heuristic(self, current, goal):
        return abs(current.x - goal.x) + abs(current.y - goal.y)

    def find_path(self, start, goal):
        start_node = Node(start[0], start[1], 0, 0)
        start_node.parent = None  # Initialize parent attribute for the starting node
        goal_node = Node(goal[0], goal[1], 0, 0)

        visited = set()
        priority_queue = [start_node]

        while priority_queue:
            current = heapq.heappop(priority_queue)

            if (current.x, current.y) == (goal_node.x, goal_node.y):
                path = []
                while current:
                    path.append((current.x, current.y))
                    current = current.parent
                return path[::-1]

            if (current.x, current.y) in visited:
                continue

            visited.add((current.x, current.y))

            for dx, dy in self.directions:
                new_x, new_y = current.x + dx, current.y + dy

                if self.is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                    new_cost = current.cost + 1
                    new_heuristic = self.calculate_heuristic(Node(new_x, new_y, 0, 0), goal_node)
                    new_node = Node(new_x, new_y, new_cost, new_heuristic)
                    new_node.parent = current
                    heapq.heappush(priority_queue, new_node)

        return None  # No path found

if __name__ == "__main__":
    # Example usage:
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    astar = AStar(grid)
    start = (0, 0)
    goal = (4, 4)

    path = astar.find_path(start, goal)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")
