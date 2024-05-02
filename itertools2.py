# itertools: product, permutations, combinations, accumulate, groupby, infinite iterators
from itertools import accumulate, groupby
import operator

# Accumulate
# 1 příklad
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)  # [1, 2, 3, 4]
print(list(acc))  # [1, 3, 6, 10]    dojde k akumulaci hodnot

# 2 příklad
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)   # multiply funkce
print(a)  # [1, 2, 3, 4]
print(list(acc))  # [1, 2, 6, 24]    1*1, 1*2, 2*3, 6*4

# 3 příklad
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)   # při poronání zobrazí větší hondnoty
print(a)  # [1, 2, 5, 3, 4]
print(list(acc))  # [1, 2, 5, 5, 5]


# Groupby
# 1 příklad
def smaller_than_3(x):
    return x < 3


a = [0, 1, 2, 3, 4, 2, 1]
group_obj = groupby(a, key=smaller_than_3)     # groupby seskupí hodnoty do jedné kombinace dle podmínky funkce smaller_than_3
for key, value in group_obj:
    print(key, list(value))     # key je True nebo False, value jsou hodnoty ze seznamu a

# True [0, 1, 2]
# False [3, 4]
# True [2, 1]

# 2 příklad (pomocí lambda funkce)
persons = [{"name": "Tim", "age": 25}, {"name": "Dan", "age": 25},
           {"name": "Lisa", "age": 27}, {"name": "Claire", "age": 28}]

group_obj = groupby(persons, key=lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))

# 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
# 27 [{'name': 'Lisa', 'age': 27}]
# 28 [{'name': 'Claire', 'age': 28}]
