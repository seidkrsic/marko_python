

# matrice 

matrica = [[1,2,3], 
          [4,5,6], 
          [7,8,9,]] 
# kako dobiti konkretno jedan element 

# x = matrica[0] 
# print(x[0])  

# bolji nacin da to uradimo 

# print(matrica[1][1])  

""" 
1 2 3 
4 5 6 
7 8 9

"""
def stampaj_matricu(matrix):
    for i in range(len(matrix)):
        print(matrix[i]) 


# stampaj_matricu(matrica) 

matrica2 = [[1,2,3], 
            [4,5,6], 
            [7,8,9]] 

# stampaj_matricu(matrica2)  


# matrica[0][0] = "Marko" 

# stampaj_matricu(matrica) 

for i in range(len(matrica2)):
    for j in range(len(matrica2)): 
        if i == j :  
            matrica2[i][j] = 1 


for i in range(len(matrica2)): 
    print(matrica2[i][0])

stampaj_matricu(matrica2) 

