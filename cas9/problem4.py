


def dodavanje_nule(n):
    
    if n == 0:
        return ''
    else:
        if (n % 10) %2 != 0:
            return dodavanje_nule(n // 10) + f"{n % 10}0"  
        else:
            return dodavanje_nule(n // 10) + f"{n % 10}" 

print(dodavanje_nule(123))