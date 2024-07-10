


from random import randint

lista=[]
for i in range(20):
    lista.append(randint(1,20))
print(lista)

for i in range(len(lista)):
    if lista[i]>=10:
        lista[i]=10
print(lista)