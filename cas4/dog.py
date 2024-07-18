


class Dog: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def aw(self): 
        print("AW AW AW!") 


dog1 = Dog("Willy", 5) 
dog2 = Dog("Ben", 6) 
print(dog1.name) 
print(dog2.aw())   