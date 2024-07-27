


# 4! = 4x3x2x1 = 24 
# n! = nx(n-1)x...x2x1 

""" 
4! = 4x3!
"""

def factorial(n): 
    if n == 1: 
        return 1 
    else: 
        return n * factorial(n-1) 


result = factorial(5) 
print(result) 