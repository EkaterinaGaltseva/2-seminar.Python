# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


n = int(input("Введите число N: "))
list = dict()
summ = 0
for i in range(1, n + 1):
    list[i] = round((1+1/i)**i, 2)
print(f'Последовательность для n = {n}: {list}\nСумма: {sum(list.values())}')
