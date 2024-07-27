

# stampamo brojeve od n do 1 

def print_numbers(n): 
    if n == 1: 
        return "1" 
    else: 
        return f"{n}\n" + print_numbers(n-1) 


# print(print_numbers(10)) 

# stampaj brojeve od 1 do n 


def printaj_brojeve(n):
    if n == 1:
        return "1\n"
    else:
        return printaj_brojeve(n-1) + f"{n}\n"

print(printaj_brojeve(13)) 