

import random

N = 10
MIN_ITEM = -1000
MAX_ITEM = 0
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range (N)]
print (array)

i = 0
index = -1
for i in range (len(array)):
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array [i] > array [index]:
        index = i

if index != -1:
    print(f'Максимальное отрицательное число {array[index]}'
          f' находится в ячейке {index}')
