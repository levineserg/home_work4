# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
n = int(input("Введите длину первого массива: "))
m = int(input("Введите длину второго массива: "))
list_1 = set()
list_2 = set()
for i in range(n):
    a = int(input("Введите число из первого массива: "))
    list_1.add(a)
for i in range(m):
    b = int(input("Введите число из второго массива: "))
    list_2.add(b)
res = []
for i in list_1:
    for j in list_2:
        if j == i:
            res.append(j)
res.sort()
for i in res:
    print(i, end=" ")
