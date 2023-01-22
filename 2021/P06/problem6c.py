import numpy as np
import numpy.linalg as la
from datetime import datetime

t1 = datetime.now()
data = open("problem6.txt", 'r').readlines()[0].strip()
data = [int(x) for x in data.split(',')]

fish = [0 for i in range(9)]

for d in data:
    fish[d] += 1

m = np.matrix([[0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0]])
M1 = la.matrix_power(m, 80)
M2 = la.matrix_power(M1, 3).dot(la.matrix_power(m, 16))
t2 = datetime.now()
print(np.sum(M1.dot(fish)))
print(np.sum(M2.dot(fish)))
print("Time: ", (t2 - t1).total_seconds())
