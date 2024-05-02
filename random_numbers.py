import random

a = random.random()   # vygeneruje náhodné číslo float
print(a)
a = random.uniform(2, 15)   # vygeneruje náhodné číslo float od 2 do 15
print(a)
a = random.randint(2, 15)  # vygeneruje náhodné číslo integer od 2 do 15 včetně těchto čísel.
print(a)
a = random.randrange(2, 15)  # vygeneruje náhodné číslo integer od 2 do 15. Bez čísla 15
print(a)

my_list = list("ABCDEFGH")
print(my_list)   # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
a = random.choice(my_list)   # vypíše jeden random element ze seznamu my_list
print(a)
a = random.sample(my_list, 3)   # vypíše tři náhodné elementy ze seznamu. Neopakují se.
print(a)   # ['G', 'C', 'D']
a = random.choices(my_list, k=3)   # vypíše tři náhodné elementy ze seznamu. Mohou se opakovat.
print(a)  # ['E', 'A', 'A']

random.shuffle(my_list)   # zamíchá obsah seznamu
print(my_list)    # ['A', 'E', 'C', 'D', 'H', 'G', 'B', 'F']

