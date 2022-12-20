# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.



numN = int(input("Введите число N: "))
list = []
import random
for i in range (1, numN +1):
    list.append(random.randint(- numN, numN))
print(list)

path = 'file.txt'
data = open(path, 'w')
data.write('2\n')
data.write('4\n')
data.close()


path = 'file.txt'
data = open(path, 'r')
mult = 1
for line in data:
    mult *= list[int(line)]
print(mult)



