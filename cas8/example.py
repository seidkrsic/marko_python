

# reccursions 

# napravimo program da napravimo mnozenje preko sabiranja 

# bez rekurzije 
        # .... 3 puta ...     
# 2*3 = 2 + 2 + 2 

def multiply(a,b): 
    sum = 0
    for _ in range(b): 
        sum += a 
    return sum 


# result = multiply(2,4) 
# print(result)  

# pomocu rekurzije 

""" 
4x5 = 4 + 4x4
"""

def rec_multiply(a,b): 
    # bazni slucaj
    if b == 1: 
        return a 
    return a + multiply(a, b-1)  

result = rec_multiply(4,5)
print(result) 







