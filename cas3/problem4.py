
from random import randint


matrica = [0]*4
matrica2 = []
for i in range(4): 
    matrica2.append(matrica)

# for i in range(len(matrix)): 
#     print(matrix[i]) 

for i in range(4):
    for j in range(4):
        matrica2[i][j] = 2

for i in range(len(matrica2)): 
    print(matrica2[i]) 

a=int(input("Broj: "))
b=int(input("Broj: "))

if matrica2[a][b] == 0:
    print("broj je 0 ")
else:
    print("broj je jedan")