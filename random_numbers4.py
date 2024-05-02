import numpy as np

a = np.random.rand(3)   # vygeneruje array
print(a)     # [0.00165055 0.03450013 0.0083956 ]

a = np.random.rand(3, 3)   # vygeneruje array s 3-dimensionalni
print(a)
# [[0.35988262 0.24269283 0.88941484]
#  [0.94559637 0.31067251 0.67995629]
#  [0.47815341 0.50992816 0.846067  ]]

a = np.random.randint(0, 10, 3)  # vygeneruje array se třemi čísly 0-10 bez 10.
print(a)    # [6 0 8]


a = np.random.randint(0, 10, (3, 4))  # když chci více dimenzí tak musím použít tuple
print(a)
#  [[6 4 9 2]
#  [2 2 9 0]
#  [5 6 5 6]]

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
#  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

np.random.shuffle(arr)   # zamíchá řádky
print(arr)
# [[4 5 6]
#  [1 2 3]
#  [7 8 9]]

# Použítí seed: Stejná funkcionalita jako u random modulu
np.random.seed(1)
print(np.random.rand(3, 3))

# [[4.17022005e-01 7.20324493e-01 1.14374817e-04]
#  [3.02332573e-01 1.46755891e-01 9.23385948e-02]
#  [1.86260211e-01 3.45560727e-01 3.96767474e-01]]

np.random.seed(1)
print(np.random.rand(3, 3))    # výjdou stejná čísla




