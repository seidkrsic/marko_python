

    # key    # value
d = {"marko": 123, "seid": 111}
print(f"markova sifra je: {d['marko']}")

for element in d.values(): # vise opcija... d.keys() ili samo d ---> elemnt je kljuc 
    print (element)         # a d.values() ---> element je value 

# best option : 
# d.items()  

username = input("username: ")
password = input("password: ")

if username in d:
    if password == str(d[username]):  # "111" === 111     str(111) ---> "111" 
        print("ulogovali ste se")
    else:
        print("korisnik postoji ali nije validna sifra")
else:
    print("korisnik ne postoji")