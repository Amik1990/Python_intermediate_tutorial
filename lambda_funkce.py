# lambda arguments: expression
# lambda se používá v případě, že ji chceme použít pouze jednou.
from functools import reduce

# 1. příklad
add10 = lambda x: x + 10
print(add10(5))

# Klasický zápis
# def add10(x):
#     return x + 10
# print(add(5))

mult = lambda x, y: x * y
print(mult(2, 6))

# 2. příklad:
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)  # defaultne se uspořádá dle první hodnoty (tzn. dle indexu 0)

print(points2D)  # [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D_sorted)  # [(1, 2), (5, -1), (10, 4), (15, 1)]

points2D_sorted = sorted(points2D, key=lambda x: x[1])  # zde chceme uspořádat dle indexu 1 (tzn. dle druhé hodnoty). X je tuple v seznamu
print(points2D_sorted)  # [(5, -1), (15, 1), (1, 2), (10, 4)]


# 3. příklad
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])  # uspořádáme dle  součtu hodnot jednotlivých tuple
print(points2D_sorted)  # [(1, 2), (5, -1), (10, 4), (15, 1)]


# 4. příklad (map funkce). a je sekvence
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)  # vynásobíme jednotlivé hodnoty krát 2. X jsou hodnoty v listu
print(list(b))  # [2, 4, 6, 8, 10]

# alternativní způsob zápisu:
c = [x * 2 for x in a]
print(c)  # [2, 4, 6, 8, 10]


# 5. příklad (filter funkce). a je sekvence
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)  # vyfiltruje sudá čísla.  x % 2 == 0 kontroluje, zda je zbytek po dělení x číslem 2 roven 0. Tedy, že se jendá o sudé číslo
print(list(b))  # [2, 4, 6]

# alternativní způsob:
c = [x for x in a if x % 2 == 0]
print(c)  # [2, 4, 6]

# moje zkouska
c = [x % 2 == 0 for x in a]
print(list(c))  # [False, True, False, True, False, True]


# 6 příklad (reduce funkce). Výstupem je jedna hodnota
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)    # 1*2 + 2*3 + 6*4 = 24    a je sekvence
print(product_a)  # 24
