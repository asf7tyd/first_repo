# №2
from itertools import permutations

lst = [1, 2, 3]
combinations = list(permutations(lst))

for c in combinations:
    print(c)
