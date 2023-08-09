# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
from random import randint

list_1 = [randint(-10, 15) for item in range(1, 15)]
min = int(input())
max = int(input())
print(list_1)
print(lst:= [i for i in range(len(list_1)) if i> min and i< max])

