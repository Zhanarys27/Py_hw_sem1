#TASK 1
# n = 125
# res = (n%10)+((n%100)//10)+(n//100)
# print(res)

#TASK2
# n = 24
# s = n//3
# print(s//2, s*2, s//2)



#TASK 3
# n = 123341
# levaya = n//1000
# pravaya = n%1000
#
# levaya = (levaya%10)+((levaya%100)//10)+(levaya//100)
# pravaya = (pravaya%10)+((pravaya%100)//10)+(pravaya//100)
# if levaya == pravaya:
#     print("yes")
# else:
#     print("no")

#TASK 4
# a, b, c = 3,5,13
# res = (a*b)
# if res>= c and (res%c) !=0:
#     print("yes")
# elif c==b and c == a:
#     print("yes")
# else:
#     print("no")



# leksia 2
# list_1 = []
# list_2 = list()
# list_3 = [1,2,4,2,6,7]
# print(list_3)
# print(*list_3)
# for i in list_3:
# #     print(i)
# print(len(list_3))
#
# list_1.append(0)
# print(*list_1)
# for i in range(5):
#     list_2.append(i)
# print(list_2)
# for i in range(3):
#     list_2.pop()
# print(list_2)
# list_2.pop(0)
# print(list_2)
# print(list_2.insert(1, 99))
# print(list_2)
# print(list_3[len(list_3)-1])
# print(list_3[:])
# print(list_3[:3])
# print(list_3[len(list_3)-2:])
# print(list_3[2:])
# print(list_3[::4])

# t = ()
# print(type(t))
# t = (1,2,3,4)
# print(type(t))
# t = list(t)
# print(t)
# print(type(t))

# a,b,c,e = t
# print(a,b,c,e)
# #
# d = {}
# d2 = dict()
# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'asdfg'
# print(d)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))# r:red g:green b:blue

#
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}

#
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# sem_2
from random import randint
#
# list_1 = [randint(0, 10) for i in range(1, 7)]
# print(list_1)
# count = 0
#
# for i in range(len(list_1)-1):
#     if list_1[i+1] > list_1[i]:
#         count += 1
#
# print(count)

# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется
# к символам с помощью постфикса формата _n.

# stroka = "assddffghjklqwerrtyasddfgghkweetwqy"
# count = 0
# stroka= list(stroka)
#
#

# print(stroka)
# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.

# text = input("input somebody text:")
# text.split()
# print(text)

# list_1 = [1, 2, 3, 4, 5]
# k = 6
#
# count = 0
# for i in list_1:
#     if i == k:
#         count+=i
#         break
#
# if count ==0:
#     for i in list_1:
#         if i + 1 == k or i == k + 1:
#             count += i
#             break
#
# print(count)
#

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
#
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k
# и выводит его. Будем считать, что на вход подается только одно слово, которое содержит
# либо только английские, либо только русские буквы.

# dict_1 = {
#     1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r', 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'],
#     2: ['d', 'g', 'д', 'к', 'л', 'м', 'п', 'у'],
#     3: ['b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я'],
#     4: ['f', 'h', 'v', 'w', 'y', 'ы', 'й'],
#     5: ['k', 'ж', 'з', 'х', 'ц', 'ч'],
#     8: ['j', 'x', 'ш', 'э', 'ю'],
#     10: ['q', 'z', 'ф', 'щ', 'ъ']
# }
# count = 0
# word = 'ящерица'
# for x in word:
#     for y in dict_1[1]:
#         if x == y:
#             count+=1
#     for z in dict_1[2]:
#         if x == z:
#             count+=2
#     for t in dict_1[3]:
#         if x == t:
#             count+=3
#     for e in dict_1[4]:
#         if x == e:
#             count+=4
#     for v in dict_1[5]:
#         if x == v:
#             count+=5
#     for w in dict_1[8]:
#         if x == w:
#             count+=8
#     for q in dict_1[10]:
#         if x == q:
#             count+=10
# print(count)


# cem 4
#   fibonachi
# def fibo(n):
#     if n in [1, 2]:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)
#
# print(fibo(8))

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# from random import randint
#
#
# list_1 = [randint(1, 5) for item in range(1, 11)]
# print(list_1)
# list_sort = sorted(list_1)
#
# print(list_sort)
# min = list_sort[0]
# max = list_sort[-1]
# for i in range(len(list_1)):
#     if list_1[i] == max:
#         list_1[i] = min
# print(list_1)

# 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*

# def is_prime(num: int) -> bool:
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for dev in range(3, num // 2 + 1, 2):
#         if num % dev == 0:
#             return False
#     return True
# is_prime(1173)

# def print_add (n):
#     if ()