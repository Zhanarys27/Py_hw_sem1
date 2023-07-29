n = int(input("Введите число: "))
list_n = []
max = 0
count = 0
for i in range(n):
    list_n.append(i+1)
for i in range(len(list_n)):
    if i == 0:
        count+= ((list_n[i-1])+list_n[i]+((list_n[i+1])))
    elif i == len(list_n)-1:
        count+= (list_n[i] + list_n[i-1] + list_n[0])
    else:
        count += ((list_n[i - 1]) + list_n[i] + ((list_n[i + 1])))
    if count>max:
        max=count
    count = 0


print(max)