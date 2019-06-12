

import random

N = 10
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range (N)]
print (array)

idx_min = 0
idx_max = 0
for i in range (len(array)):
    if array [i] < array [idx_min]:
        idx_min = i
    elif array [i] > array [idx_max]:
        idx_max = i

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print (array)
