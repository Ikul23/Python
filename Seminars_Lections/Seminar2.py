# # # # # ДЗ 1

# # # # # Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# # # # # решкой, а некоторые – гербом. Определите минимальное число
# # # # # монеток, которые нужно перевернуть, чтобы все монетки были
# # # # # повернуты вверх одной и той же стороной. Выведите минимальное
# # # # # количество монет, которые нужно перевернуть.
# # # # # 5 -> 1 0 1 1 0
# # # # # 2
# # # # # qm = int(input('введите количество монет'))

# # # # # print(*range(0,qm+1),1)

# # # # # Петя и Катя – брат и сестра. Петя – студент, а Катя –
# # # # # школьница. Петя помогает Кате по математике. Он задумывает два
# # # # # натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# # # # # этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# # # # # произведение P. Помогите Кате отгадать задуманные Петей числа.

# # # # # sum = int(input ("Введите сумму чисел x и y"))
# # # # # mult = int(input ("Введите произведение чисел x и y"))

# # # # # if sum - x 

# # # # # n = int(input ('Введите натуральное число: '))
# # # # # # p = n // 4
# # # # # # s = n // 4
# # # # # # k = n - p - s
# # # # # print (n//4, n-(n//4*2), n//4, end='')
# # # n = 385916
# # # n1 = n//100000 + (n//10000)%10 + (n//1000)%10
# # # n2 = (n//100)%10 + (n//10)%10 + n%10 
# # # if n1 == n2:
# # #     print('yes')
# # # else:
# # #     print('no')
# # # Задача 3: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# # # не превосходящие числаN.
# # n = 16
# # # k = -1
# # # p = 0
# # # while p < n:        
# # #     k = k + 1   
# # #     p =  2 ** k
# # #     print(p)   
# # i = 0
# # while 2 ** i <= n:
# #     print(2 ** i)
# #     i += 1



# # # # # ДЗ 2
# # # # # Задача8
# # # # # n = int (input ('Введите количество долек по горизонтали:'))
# # # # # m = int (input ('Введите количество долек по вертикали:'))
# # # # # k = int (input ('Введите количество долек:'))
# # # # # if n*m >= k and (n*m % k == 0 or (n*m - k) % 2 == 0):
# # # # #     print ('Yes')
# # # # # else:
# # # # #     print ('No')

# Напишите программу, которая принимает от пользователя число n, кол-во элементов списка.
# # Затем пользователь вводит на каждой новой строчке число, которое необходимо сохранить в список.
# n = int(input("Введите кол-во элементов списка: "))
# data = []
# for i in range(n):
#     data.append(int(input("Введите число: ")))
#     # insert(position, element)
# print(*data)

# List comprehansive
# print(*[i for i in range(5)])
print(*[(i, i**2) for i in range(5)]) # запись через кортеж


