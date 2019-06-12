

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9

for i in range (START_DIV, END_DIV + 1):
    frequency = 0
    for j in range (START_NUM, END_NUM + 1):
        if j % i == 0:
            frequency += 1
    print(f'Числу {i} кратно {frequency} чисел')
