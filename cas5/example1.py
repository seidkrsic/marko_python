

class Wizzard: 
    def __init__(self, name): 
        self.name = name 

    def info(self): 
        print(f"{self.name}") 
        try: 
            print(self.subject) 
        except AttributeError: 
            print("No subject for this wizzard") 


class Professor(Wizzard): 
    def __init__(self, name, subject): 
        super().__init__(name)  
        self.subject = subject 



wizzard = Wizzard("Marko")
wizzard.info() 
professor = Professor("Seid", "Python") 
print(professor.info())  









