# Задача 14.
# Требуется вывести все целые степени двойки (т.е. числа вида 2 k ), не превосходящие числа N.
# 10 -> 1 2 4 8

print()
n = int(input("Введите число N: "))
print()

i = 0
output_num = ""
while 2 ** i <= n:
    output_num += str(i) + ", "
    i += 1
output_num = output_num[:-2]

print('Целые степени двойки числа', n,'это:', output_num)
print()
