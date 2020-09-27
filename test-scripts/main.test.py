import numpy as np

rolls = np.random.randint(low=1, high=6, size=10)
arr = np.array([1, 2, 3, 4, 5])

print(rolls)
print(rolls <= 3)

print(rolls + 10)