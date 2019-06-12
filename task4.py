

import random

N = 100
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range (N)]
print (array)

counter = {}
frequency = 1
num = None
for item in array:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1

    if counter[item] > frequency:
        counter[item] = frequency
        num = item

if num is not None:
    print (f'Число {num} повторяется {frequency} раз')
else:
    print('Числа не повторяются')
