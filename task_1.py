# task 1  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
from random import randint
n = int(input("Введите количество монет: "))
orel = 0
reshka = 0
for _ in range(n):
    monety = randint(0, 1)
    print(monety, end=' ')
    if monety == 1:
        reshka +=1
    else:
        orel +=1
if reshka > orel:
    print(f"\nЛегче перевернуть орла, так как орел меньше: {orel} монеток")
elif reshka == orel:
    print("\nВсе равно что переворачивать они равны")
elif reshka == n or orel == n:
    print("Можно и не переворачивать, тебе повезло!")
else:
    print(f"\nЛегче перевернуть решку, так как решка меньше: {reshka} монеток")
