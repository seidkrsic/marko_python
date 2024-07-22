

class Student: 
    # class variable 
    total_students = 0 

    # instance method 
    def __init__(self, name): 
        self.name = name 
        self.grades = []
        Student.total_students += 1

    # instance method 
    def add_grade(self, grade): 
        self.grades.append(grade) 

    # class method here 
    @classmethod
    def student_count(cls): 
        return cls.total_students 
    

    # static method here 
    @staticmethod 
    def calculate_average(grades): 
        if not grades: 
            return 0  
        else: 
            return round(sum(grades) / len(grades), 2) 


student1 = Student("Marko") 
student2 = Student("Seid") 

student1.add_grade(4) 
student1.add_grade(3) 
student1.add_grade(3) 
student1.add_grade(2) 


student2.add_grade(3) 
student2.add_grade(3) 
student2.add_grade(2) 
student2.add_grade(4) 

print(Student.calculate_average(student1.grades))

# print(Student.student_count() )