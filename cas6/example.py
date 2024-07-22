



lista = [] 

person = {"name" : "Marko", "telephone": "123"} 
person1 = {"name" : "Seid", "telephone": "1234"} 
lista.append(person) 
lista.append(person1) 
for person in lista: 
    print(person["name"], person["telephone"])   