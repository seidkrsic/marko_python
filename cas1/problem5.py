
from random import randint
lista=[]
for i in range(20):
    lista.append(randint(1,10))
a = 0
for number in lista:
    a += number

print(a/len(lista))
lista.sort()
print(lista)

print(lista[0])
print(lista[-1])