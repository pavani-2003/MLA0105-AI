import itertools
import sys

def calculate_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def total_distance(tour, cities):
    distance = 0
    for i in range(len(tour) - 1):
        distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    distance += calculate_distance(cities[tour[-1]], cities[tour[0]])  # Return to the starting city
    return distance

def traveling_salesman_bruteforce(cities):
    num_cities = len(cities)
    if num_cities < 2:
        print("Error: There must be at least two cities.")
        return None

    # Generate all possible tours using itertools.permutations
    all_tours = list(itertools.permutations(range(num_cities)))

    # Find the tour with the minimum total distance
    min_distance = sys.maxsize
    optimal_tour = None

    for tour in all_tours:
        distance = total_distance(tour, cities)
        if distance < min_distance:
            min_distance = distance
            optimal_tour = tour

    return optimal_tour, min_distance

if __name__ == "__main__":
    # Example usage:
    cities = [(0, 0), (1, 2), (2, 4), (3, 1), (5, 3)]

    result = traveling_salesman_bruteforce(cities)

    if result:
        optimal_tour, min_distance = result
        print("Optimal Tour:", optimal_tour)
        print("Minimum Distance:", min_distance)
