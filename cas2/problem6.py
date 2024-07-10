


from random import randint

lista=[]
for i in range(10):
    lista.append(randint(1,10))
x=[]
for number in lista:
    if number not in x:
        x.append(number)
        
print(x)