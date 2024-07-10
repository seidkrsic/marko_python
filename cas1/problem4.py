

from random import randint
lista=[]
for i in range(10):
    lista.append(randint(1, 10))
print(lista)

for i in range(len(lista)):
    lista[i] = lista[i] **2
print(lista)

print(f"Lista ima {len(lista)} elemenata") 
                                #  0 1 2  
# posljednji element liste    l = [1,2,3]
print(lista[len(lista) - 1])  # print(lista[-1]) 

lista.reverse() 
print(lista) 
lista.sort() 
print(lista) 

if 5 in lista: 
    print("YEs") 
else: 
    print("NO!") 

