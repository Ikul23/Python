# # 
# Задача пишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# data = input('введите символы через пробел: ').split()
# print(data)
# freq_dict = {}
# for i in data: #проходим по списку
#     if i not in freq_dict.keys():
#         print(i, end=' ')
#         freq_dict[i]=1
#     else:
#         print(f'{i}_{freq_dict[i]}', end=' ')
#         freq_dict[i] +=1

print([chr(i) for i in range(ord("А"), ord("Я") + 1)])