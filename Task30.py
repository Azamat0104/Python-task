# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input("Введите первый член арифметической прогрессии: "))
d = int(input("Введите шаг арифметической прогрессии: "))
n = int(input("Введите количество членов арифметической прогрессии: "))

progression = [a1]
for i in range (1, n):
    progression.append(progression[i-1] + d)

print(f"Ваша прогрессия: {progression}")