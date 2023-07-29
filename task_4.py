n_1 = int(input("Введите размерность n: "))
m_1 = int(input("Введите размерность m: "))
list_n = []
for i in range(n_1):
    list_n.append(int(input("Введите элементы множеств n: ")))
n = set(list_n)
list_m =[]
for i in range(m_1):
    list_m.append(int(input("Введите элементы множеств m: ")))
m = set(list_m)
print(n, m)
list_n = list(n)
list_m = list(m)
print(list_n.sort())
print(list_m.sort())
z = n & m
list_z = list(z)
print(list_z.sort())


