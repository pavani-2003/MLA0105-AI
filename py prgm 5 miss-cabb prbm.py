from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0:
            return False
        if self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if 3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries > 0:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return (
            self.missionaries == other.missionaries and
            self.cannibals == other.cannibals and
            self.boat == other.boat
        )

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def get_neighbors(state):
    neighbors = []
    if state.boat == 1:
        # Moving from the initial side to the other side
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(state.missionaries - m, state.cannibals - c, 0)
                    if new_state.is_valid():
                        neighbors.append(new_state)
    else:
        # Moving from the other side to the initial side
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(state.missionaries + m, state.cannibals + c, 1)
                    if new_state.is_valid():
                        neighbors.append(new_state)
    return neighbors

def solve_missionaries_cannibals():
    initial_state = State(3, 3, 1)
    goal_state = State(0, 0, 0)

    queue = deque([([initial_state], [])])

    while queue:
        current_path, actions = queue.popleft()
        current_state = current_path[-1]

        if current_state.is_goal():
            return actions

        for neighbor in get_neighbors(current_state):
            if neighbor not in current_path:
                new_path = current_path + [neighbor]
                new_actions = actions + [(neighbor.missionaries - current_state.missionaries, neighbor.cannibals - current_state.cannibals, neighbor.boat)]
                queue.append((new_path, new_actions))

    return None

def print_solution(actions):
    if actions is None:
        print("No solution found.")
    else:
        print("Solution:")
        for action in actions:
            print(f"{action[0]} missionaries and {action[1]} cannibals move {'from' if action[2] == 1 else 'to'} the other side.")

if __name__ == "__main__":
    solution = solve_missionaries_cannibals()
    print_solution(solution)
