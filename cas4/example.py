

class Student: 
    def __init__(self, first_name, last_name): 
        self.first_name = first_name 
        self.last_name = last_name 


def main(): 
    student = get_student() 
    print(student.first_name)     

# lista = [1] 
# lista[0] = marko 
# tuple = (12,2,3,33) 
    # tuple[0] = marko ### NE MOZE! 

def get_student():
    first = input("Unesi ime: ") 
    last = input("Unesi prezime: ") 
    return Student(first, last) 
    




if __name__ == "__main__":
    main()  



