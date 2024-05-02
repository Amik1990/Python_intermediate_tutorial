import sys
import timeit

# 1. Přídklad
my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple
print(name)
print(age)
print(city)

# 2. Příklad
my_tuple2 = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple2    # hvězdička se použije když chci vypsat víc jak jednu hodnotu
print(i1)
print(i3)
print(i2)     # vypíše hodnoty jako seznam: [1, 2, 3]

# Důkaz, že tuple bere méně místa než seznam
my_list = [0, 1, 2, "Hello", True]
my_tuple = (0, 1, 2, "Hello", True)
print(sys.getsizeof(my_list), "bytes")    #104 bytes
print(sys.getsizeof(my_tuple), "bytes")   #80 bytes


# Důkaz, že tuple se vygeneruje rychleji než seznam: Spočítáme za jak dlouho vygeneruje milionkrát seznam a tuple
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))   #0.09489760012365878
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))   #0.026142899878323078
