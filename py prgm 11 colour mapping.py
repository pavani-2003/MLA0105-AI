class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, assignment, var, value):
        for constraint in self.constraints[var]:
            if constraint[0] in assignment and not constraint[1](value, assignment[constraint[0]]):
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment  # Solution found

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(assignment, var, value):
                assignment[var] = value
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None  # No solution found

    def select_unassigned_variable(self, assignment):
        unassigned_vars = [var for var in self.variables if var not in assignment]
        return min(unassigned_vars, key=lambda var: len(self.domains[var]))

    def order_domain_values(self, var, assignment):
        return self.domains[var]

def not_equal_constraint(value, assigned_value):
    return value != assigned_value

if __name__ == "__main__":
    # Example usage: Map Coloring Problem
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {var: ['R', 'G', 'B'] for var in variables}
    constraints = {
        'WA': [('NT', not_equal_constraint), ('SA', not_equal_constraint)],
        'NT': [('WA', not_equal_constraint), ('SA', not_equal_constraint), ('Q', not_equal_constraint)],
        'SA': [('WA', not_equal_constraint), ('NT', not_equal_constraint), ('Q', not_equal_constraint), ('NSW', not_equal_constraint), ('V', not_equal_constraint)],
        'Q': [('NT', not_equal_constraint), ('SA', not_equal_constraint), ('NSW', not_equal_constraint)],
        'NSW': [('SA', not_equal_constraint), ('Q', not_equal_constraint), ('V', not_equal_constraint)],
        'V': [('SA', not_equal_constraint), ('NSW', not_equal_constraint)],
        'T': []
    }

    map_coloring_csp = CSP(variables, domains, constraints)
    solution = map_coloring_csp.backtracking_search()

    if solution:
        print("Map Coloring Solution:")
        for var, color in solution.items():
            print(f"{var}: {color}")
    else:
        print("No solution found.")
