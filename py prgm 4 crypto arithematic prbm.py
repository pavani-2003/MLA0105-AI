import itertools

def is_valid_assignment(mapping, words, result):
    # Check if the current assignment is valid
    num1 = sum(mapping[c] * 10**i for i, c in enumerate(reversed(words[0])))
    num2 = sum(mapping[c] * 10**i for i, c in enumerate(reversed(words[1])))
    res = sum(mapping[c] * 10**i for i, c in enumerate(reversed(result)))

    return num1 + num2 == res

def solve_cryptarithmetic(words, result):
    # Extract unique letters from the words and result
    unique_letters = set("".join(words) + result)

    # Check if the lengths of the unique letters and the set of all digits are equal
    if len(unique_letters) > 10:
        print("Invalid Cryptarithmetic problem. Too many unique letters.")
        return None

    # Generate all possible digit assignments to letters
    digit_assignments = itertools.permutations(range(10), len(unique_letters))

    for assignment in digit_assignments:
        mapping = dict(zip(unique_letters, assignment))

        if is_valid_assignment(mapping, words, result):
            return mapping

    print("No solution found.")
    return None

if __name__ == "__main__":
    words = ["send", "more"]
    result = "money"

    solution = solve_cryptarithmetic(words, result)

    if solution:
        print("Solution found:")
        for word in words + [result]:
            print(f"{word}: {''.join(str(solution[c]) for c in word)}")
    else:
        print("No solution found.")
