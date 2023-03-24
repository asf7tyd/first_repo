from itertools import permutations

numbers = [1, 2, 3]

combinations = list(permutations(numbers))

for combination in combinations:
    print(combination)
