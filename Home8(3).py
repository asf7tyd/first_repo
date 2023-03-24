# №4
import random

lst = random.sample(range(1, 10), 5)
combinations = [(a, b, c, d, e) for a in lst for b in lst if b != a for c in lst if c not in (a, b) for d in lst if
                d not in (a, b, c) for e in lst if e not in (a, b, c, d)]

for c in combinations:
    print(c)
