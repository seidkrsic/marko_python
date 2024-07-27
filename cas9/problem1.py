

def broj_cifara(n):
    if n == 0:
        return 0
    else:
        return 1 + broj_cifara(n//10)
    
print(broj_cifara(1235))

