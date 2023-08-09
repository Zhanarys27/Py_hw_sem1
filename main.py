# TASK 1
# n = 125
# res = (n%10)+((n%100)//10)+(n//100)
# print(res)

# TASK2
# n = 24
# s = n//3
# print(s//2, s*2, s//2)


# TASK 3
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

# TASK 4
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


# lektion
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res +=i
#     return res
#
# print(sum_str('1','v', 'ew', 'ter' ))


# vozvedenie v stepen

# def f(a,b):
#     if b == 1:
#         return a
#     else:
#         return a*f(a, b-1)
#
# a, b = int(input()), int(input())
# print(f(a, b))

# def sum(a,b):
#     if b ==1:
#         return a
#     else:
#         return a+sum(a,b-1)
# a = 2
# b = 2
# print(sum(a, b))
#
# def sum(n):
#     if n<1:
#         return ''
#     i = input()
#     return sum(n-1)+' '+i
# n = int(input())
# print(sum(n))


# list_1 = [1,2,3,4,5,7,8,44, 38]
# for i in list_1:
#     if i %2==0:
#         print(lambda: i*i, i)


# def calc2(x):
#     return x * 10
#
#
# def math(op, x):
#     print(op, x)
#
#
# math(calc2, 10)  # 100

# list_1 = [x for x in range(1,20)]
# print(list_1)
# list_1= list(map(lambda x: x+10, list_1))
# print(list_1)



# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
#
# transformation = <???>
#
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
#
# transormed_values = list(map(transformation, values))
#
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
#
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
#
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
#


# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты
# не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены
# на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой
# планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется
# по формуле S = piab, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка:
# проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам
#  эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

# import math
# from random import randint
#
# lst = [(randint(1, 10), randint(1, 10)) for i in range(5)]
#
#
# def find_farthest_orbit(list_of_orbits):
#     list_res = []
#     for i,j in list_of_orbits:
#         if i != j:
#             S = math.pi * i * j
#             list_res.append(S)
#     max_s = max(list_res)
#
#     res = list_of_orbits[list_res.index(max_s)]
#     print(list_res)
#     return res
#
# print(lst)
# print(find_farthest_orbit(lst))
#
# import random
#
# print(planets := [(random.randint(1,10), random.randint(1, 10)) for _ in range(10)])
#
# planets = list(filter(lambda x: x[0] != x[1], planets))
# print(planets)
#
# print(max(planets, key = lambda x: x[0]*x[1]))


# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел -
# элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
from random import randint


# def sort(list_1, list_2):
#     res_list = []
#     for i in list_1:
#         if i not in list_2:
#             res_list.append(i)
#     return res_list
#
# n = int(input())
# list_1 = [randint(1, 10) for item in range(1, n+1)]
# m = int(input())
# list_2 = [randint(1, 10) for item in range(1, m+1)]
# print(list_1)
# print(list_2)
# print(sort(list_1, list_2))

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве
# определит количество элементов, у которых два соседних и, при этом, оба соседних
# элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# n = int(input())
# list_1 = [randint(1, 10) for item in range(1, n+1)]
# res_list = []
# print(list_1)
# for i in range(len(list_1)):
#     if i == 0:
#         continue
#     elif  list_1[i+1]<list_1[i] > list_1[i-1] :
#         res_list.append(list_1[i])
#     elif i == len(list_1)-2:
#         break
# print(len(res_list))



# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# n = int(input())
# list_1 = [randint(1, 10) for item in range(1, n+1)]
# res = 0
# count = 0
# print(list_1)
# for i in list_1:
#     count = list_1.count(i)
#     if count > 1:
#         res += count//2
#     count = 0
# print(res//2)
# print(list_1)
# for i in set(list_1):
#     count+=list_1.count(i)//2
# print(count)


# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести
# все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной
# в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# def sum_devs(n: int):
#     count = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             count += i
#     return count
#
#
# digit_dict = {i: sum_devs(i) for i in range(1, 10000)}
#
# for digit, summ_ in digit_dict.items():
#     if digit == digit_dict.get(summ_) and digit<summ_:
#         print(digit, summ_)
