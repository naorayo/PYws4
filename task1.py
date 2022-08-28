""" Задайте строку из набора чисел. Напишите программу,
которая покажет большее и меньшее число. В качестве
символа-разделителя используйте пробел.
"""

list = input('Введи числа через пробел: ').split()
list = [int(x) for x in list]
max = list[0]
min = list[0]

for i in range(1, len(list)):
	if list[i] > max:
		max = list[i]
	if list[i] < min:
		min = list[i]

print(f'ВведенЫ список: {list}\nМинимальный элемент: {min}\nМаксимальный элемент: {max}')