# infinite iterators
from itertools import count, cycle, repeat

# Count metoda
for i in count(10):
    print(i)
    if i == 15:   # vypíše čísla od 10 do 15
        break

# 10
# 11
# 12
# 13
# 14
# 15

# Cycle metoda. Bude iterovat dokola 123
# a = [1, 2, 3]
# for i in cycle(a):
#     print(i)


# Repeate metoda:
a = [1, 2, 3]
for i in repeat(1, 4):   # vypíše 1  4krát
    print(i)


for i in repeat(1):   # bude pořád psát 1
    print(i)
