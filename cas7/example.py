

# instance methods ... to su ovi standardni methodi koje smo pravili 



class MyClass: 
    # class variable 
    total_num_of_elements = 0

    def __init__(self, name):
        self.name = name 

    # instance method
    def instance_method(self): 
        print("This is instance method") 

    # class method 
    @classmethod
    def class_method(cls): 
        print("This is class method... it can print total num of elements of this class: ")
        print(cls.total_num_of_elements) 

    # static method 
    @staticmethod
    def static_method(x, y): 
        print(x+y) 




object = MyClass("DOg") 
object.instance_method() 
MyClass.class_method() 
MyClass.static_method(2,3) 