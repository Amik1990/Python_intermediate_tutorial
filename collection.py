# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
a = "aaaaabbbccc"
my_counter = Counter(a)
print(my_counter)   # Counter({'a': 5, 'b': 3, 'c': 3})
print(my_counter.items())  # dict_items([('a', 5), ('b', 3), ('c', 3)])
print(my_counter.keys())  # dict_keys(['a', 'b', 'c'])
print(my_counter.values())  # dict_values([5, 3, 3])
print(my_counter.most_common(1))  # vypíše nejpouživanější objekt   [('a', 5)]
print(my_counter.most_common(2))  # vypíše dva nejpouživanější objekty    [('a', 5), ('c', 5)]
print(my_counter.most_common(1)[0])  # vypíše první element ze seznamu, index je 0.  Výjde  ('a', 5)
print(my_counter.most_common(1)[0][0])  # vypíše první hodnotu z objektu. tzn a .  Je to a  z objektu ('a', 5)

print(list(my_counter.elements()))  # vypíše hodnoty do seznamu, jako iterace. Musíme ale převést na list

# namedtuple
Point = namedtuple("Point", "x,y")     # vytvořím třídu Point s hodnotami x, y
pt = Point(1, -4)
print(pt)   # Point(x=1, y=-4)
print(pt.x, pt.y)  # 1 -4

# OrderedDict   je to samé jako slovník, ale zde si pamatuje v jaké pořadí jsme vkládali hodnoty do slovníku
# V nových verzích pythonu klasické slovníky si pamatují pořadí.

# Defaultdict
d = defaultdict(int)  # nastavím defaultní hodnotu slovníku jako integer. Mohu použít i bool, list, atd
d["a"] = 1
d["b"] = 3
print(d)   # defaultdict(<class 'int'>, {'a': 1, 'b': 3})
print(d["a"])   # 1
print(d["c"])   # výjde nula, protože klíč c neexistuje a jako defaultní hodnotu máme integer tak se vygeneruje 0

# kdybych měl nastavený prázdný slovník d = {}, tak by se mi zobrazila chyba, při zadání klíče c.


# Deque umožňuje vkládat a odstraňovat hodnoty do seznamu z levé i pravé strany
d = deque()

d.append(1)
d.append(2)
d.appendleft(5)
print(d)  # deque([5, 1, 2])
d.pop()
print(d)  # deque([5, 1])
d.popleft()
print(d)  # deque([1])
d.clear()  # odstraní všechny hodnoty.    deque([])
print(d)
d.extend([7, 8, 9])   # vkládá hodnoty z pravé strany
print(d)  # deque([7, 8, 9])
d.extendleft([4, 5])   # vkládá hodnoty z levé strany
print(d)   # deque([5, 4, 7, 8, 9])
d.rotate(1)  # rotuje hodnoty o jeden doprava
print(d)    # deque([9, 5, 4, 7, 8])
d.rotate(-2)  # rotuje hodnoty o dva doleva
print(d)   # deque([4, 7, 8, 9, 5])

