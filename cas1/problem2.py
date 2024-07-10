

# korisnik unosi broj i ako unese neparan broj kvadriramo ga, a ako unese paran stepen 3 


a = int(input("unesite broj: "))

if a % 2 == 0:
    x = a**2
else:
    x= a**3
print(x)