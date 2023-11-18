from collections import deque

def water_jug_problem(capacity_jug1, capacity_jug2, target):
    visited_states = set()
    queue = deque([(0, 0)])

    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        if current_state == target:
            return reconstruct_path(current_state)

        visited_states.add(current_state)

        # Fill jug 1
        fill_jug1 = (capacity_jug1, jug2)
        if fill_jug1 not in visited_states:
            queue.append(fill_jug1)

        # Fill jug 2
        fill_jug2 = (jug1, capacity_jug2)
        if fill_jug2 not in visited_states:
            queue.append(fill_jug2)

        # Empty jug 1
        empty_jug1 = (0, jug2)
        if empty_jug1 not in visited_states:
            queue.append(empty_jug1)

        # Empty jug 2
        empty_jug2 = (jug1, 0)
        if empty_jug2 not in visited_states:
            queue.append(empty_jug2)

        # Pour water from jug 1 to jug 2
        pour_jug1_to_jug2 = (max(0, jug1 - (capacity_jug2 - jug2)), min(capacity_jug2, jug1 + jug2))
        if pour_jug1_to_jug2 not in visited_states:
            queue.append(pour_jug1_to_jug2)

        # Pour water from jug 2 to jug 1
        pour_jug2_to_jug1 = (min(capacity_jug1, jug1 + jug2), max(0, jug2 - (capacity_jug1 - jug1)))
        if pour_jug2_to_jug1 not in visited_states:
            queue.append(pour_jug2_to_jug1)

    return None

def reconstruct_path(final_state):
    path = [final_state]
    while final_state != (0, 0):
        if final_state[0] == 0:
            path.append((final_state[0], final_state[1]))
            final_state = (final_state[0], 0)
        elif final_state[1] == 0:
            path.append((final_state[0], final_state[1]))
            final_state = (0, final_state[1])
        elif final_state[0] > 0:
            path.append((final_state[0], final_state[1]))
            final_state = (0, final_state[1])
        elif final_state[1] > 0:
            path.append((final_state[0], final_state[1]))
            final_state = (final_state[0], 0)
    path.reverse()
    return path

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_state = (2, 0)

    solution_path = water_jug_problem(jug1_capacity, jug2_capacity, target_state)

    if solution_path:
        print(f"Solution found! Steps to reach {target_state}:")
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}: Jug 1: {state[0]}, Jug 2: {state[1]}")
    else:
        print(f"No solution found to reach {target_state} with given jug capacities.")
