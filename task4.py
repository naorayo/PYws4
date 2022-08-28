""" Найдите корни квадратного уравнения Ax² + Bx + C = 0
с помощью математических формул нахождения корней квадратных уравнений.
"""


import math

print("Введите коэффициенты уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
	x1 = (-b - math.sqrt(discr)) / (2 * a)
	x2 = (-b + math.sqrt(discr)) / (2 * a)
	print('Корни уравнения: \nx1 = %.2f \nx2 = %.2f' % (x1, x2))
elif discr == 0:
	x = -b / (2 * a)
	print('Корень уравнения: x = %.2f' % x)
else:
	print("Нет действительных корней")

