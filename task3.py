""" На вход поступает список из целых чисел и
отдельно число target. Нужно найти индексы таких
двух чисел из списка, которые в сумме равны target.
"""

class Solution(object):
	def twoSum(self, nums, target):
		mapping = {}
		for index, val in enumerate(nums):
			difference = target - val
			if difference in mapping:
				return [mapping[difference], index]
			else:
				mapping[val] = index

s = Solution()
list = input('Введи числа списка через пробел: ').split()
list = [int(x) for x in list]
target = int(input('Введи число target: '))

print(f'Индексы элементов: {s.twoSum(list, target)}')