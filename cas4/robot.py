

class Robot:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    
    def info(self):
        print(f"moje ime je {self.name}, {self.color} sam boje i imam {self.age} godina")


a = Robot("Bob", "blue", "13")
print(a.name)
a.info()