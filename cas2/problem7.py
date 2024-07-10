


# unosi a 
a = int(input("Unesi a: "))

# unosi n 

n = int(input("unesi n: "))

# stampamo n brojeva vecih od a koji su djeljivi sa 11 

p = a 
i = 0
while i<n: 
    if p % 11 == 0 and p > a:
        print(p) 
        i += 1 
        p += 1 
    else: 
        p += 1 