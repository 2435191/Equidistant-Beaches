#https://fivethirtyeight.com/features/can-you-reach-the-beach/
#(riddler express)

import time

from numpy import arange
from math import isclose
from itertools import combinations

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


# find all equidistant points
print('starting')
start = time.time()

x_list = []
y_list = []
for x in arange(0.0, 3.0, 0.01):
    for y in arange(0.0, 2.0, 0.01):
        measurements = [x, y, 3.0 - x, 2.0 - y] # distances from each beach
        for tup in combinations(measurements, 2):
            if isclose(tup[0], tup[1], abs_tol=0.001):
                x_list.append(round(x, 2))
                y_list.append(round(y, 2))


print(f'done in {time.time()-start}')

# graph it

plt.scatter(x_list, y_list, s=5, c='black', marker='.')

plt.show()