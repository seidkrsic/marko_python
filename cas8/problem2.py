



# izracunaj 1+2+3+... + n = ? 
# rekurzivno 

# 1 + 2 + 3 + .... + 9 + 10 = 
def suma(n): 
    if n == 1: 
        return 1   
    else: 
        return n + suma(n-1)  

# result = suma(100) 
# print(result) 

# izracunaj zbir elemenata iz liste 
# [1,2,3,4,5] ----> 1 + [2,3,4,5] ..... nakon dosta koraka --- > [5] 
def sum_of_list_elements(n): 
    """ 
    n: list 
    return: int 
    """
    if len(n) == 1: 
        return n[0] 
    else: 
        return n[0] + sum_of_list_elements(n[1:])  




def multiplication_of_lista(n):

    if len(n) == 1:
        return n[0]
    else:
        return n[0] * multiplication_of_lista(n[1:])


result = multiplication_of_lista([1,2,3,4,5]) 
print(result) 