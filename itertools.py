# itertools: product, permutations, combinations, accumulate, groupby, infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement
# Product
# 1. příklad
a = [1, 2]
b = [3, 4]
prod = product(a,b)
print(prod)  # <itertools.product object at 0x000001A14E914F80>   musím změnit na list, aby se správně zobrazilo
print(list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]

# 2 příklad
a = [1, 2]
b = [3]
prod = product(a,b, repeat= 2)
print(list(prod))  # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

# Permutations
# 1 příklad:
a = [1, 2, 3]
perm = permutations(a)   # permutation vypíše věechny kombinace čísel v množině a
print(list(perm))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm = permutations(a, 2)    # délka 2. Tzn omezíme kombinace čísel na dvě položky
print(list(perm))   # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Combinations
# 1 příklad
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# 2 příklad
a = [1, 2, 3, 4]
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))   # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

