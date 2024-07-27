

# 123 ---> 3 2 1 
# 

def prikaz_broja_s_lijeva(n): 
    if n == 0: 
        return "" 
    else: 
        return  f"{n % 10}\n" + prikaz_broja_s_lijeva(n // 10) 

print(prikaz_broja_s_lijeva(123) ) 

