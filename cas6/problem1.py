

class Contestant: 
    total_pies_eaten = 0

    def __init__(self, name): 
        self.name = name 
        self.pies_eaten = 0 
    
    def eat_pie(self): 
        self.pies_eaten += 1
        Contestant.total_pies_eaten += 1
    


if __name__ == "__main__" : 
    alice = Contestant("Alice") 
    bob = Contestant("Bob") 

    alice.eat_pie() 
    bob.eat_pie() 
    alice.eat_pie() 
    print(f"Bob has eaten {bob.pies_eaten}")
    print(f"Alice has eaten {alice.pies_eaten}")
    print(f"Total pies eaten: {Contestant.total_pies_eaten}")  


