import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_neighbors(node):
    neighbors = []
    i, j = find_blank(node.state)

    for action in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + action[0], j + action[1]

        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in node.state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, node, action, node.cost + 1, heuristic(new_state)))

    return neighbors

def heuristic(state):
    # Manhattan distance heuristic
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    h = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            gi, gj = divmod(value, 3)
            h += abs(i - gi) + abs(j - gj)
    return h

def solve_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state, None, None, 0, heuristic(initial_state))
    priority_queue = [initial_node]
    visited_states = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.state == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            return build_solution(current_node)

        visited_states.add(tuple(map(tuple, current_node.state)))

        neighbors = generate_neighbors(current_node)
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor.state)) not in visited_states:
                heapq.heappush(priority_queue, neighbor)

    return None

def build_solution(node):
    solution = []
    while node.parent:
        solution.append((node.action, node.state))
        node = node.parent
    solution.reverse()
    return solution

def print_solution(solution):
    for step, state in solution:
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()

if __name__ == "__main__":
    initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    solution = solve_puzzle(initial_state)

    if solution:
        print("Solution found!")
        print_solution(solution)
    else:
        print("No solution found.")
