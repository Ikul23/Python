# 
# Множества
# Множества содержат в себе уникальные элементы, не обязательно
# упорядоченные.
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}


# Лекция 4: Функции высшего
# порядка, работа с файлами.

# def calc1(x):
#     return x + 10
# def calc2(x):
#     return x * 10
# def math(op, x):
#     print(op, x)
# math(calc2, 10) 

# Функции map(), lambda(), filter()
# Задача 1. В списке хранятся числа. Нужно выбрать только чётные числа и 
# составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = input('Введите числа: ')
# data = list(map(int, data.split()))
# print(data)

# data_1 = list(filter(lambda x: x % 2 == 0, data))
# print(data_1)

# data_new = list(map(lambda x: (x, x ** 2), data_1))
# print(data_new)

# Функция zip()

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)

# Функция reduce() в Python является частью модуля functools и используется для последовательного применения функции 
# к элементам итерируемого объекта, сокращая его до одного значения. 

# from functools import reduce

# # Пример: нахождение суммы элементов списка
# numbers = [1, 2, 3, 4, 5]
# sum_result = reduce(lambda x, y: x + y, numbers)
# print(sum_result)

# Функция enumerate() позволяет пронумеровать набор данных.

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)

# Задаем функцию def:
# def sum_numbers(n, y = 'Hello'):
#     print(y) # задаем функцию
#     summa = 0
#     for i in range(1, n+1):
#         summa+=i
#     return summa # возвращаем нашу функцию

# print(sum_numbers(5, 'data')) # вводим данные в функцию

# Пример: функция, которая принимает неограниченное количество аргументов:
# def sum_str (*args):
#     res = ''
#     for i in args:
#         res+=i 
#     return res
# print(sum_str('5' 'w' '5678' 'erw'))
# print(sum_str('5' 'w' '5678' 'erw' '5' 'w' '5678' 'erw'))

# Рекурсия