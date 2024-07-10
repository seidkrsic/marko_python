


a = int(input("unesite broj: "))
b= int(input("unesite broj: "))

x=0
sum=0

for i in range(a, b+1):
    if i %2 != 0:
        x+=1
        sum = sum + i 
print(sum/x)
