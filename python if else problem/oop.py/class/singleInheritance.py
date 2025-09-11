# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        # Calling Parent Constructor using super()
        super().__init__(name, age)
        self.student_id = student_id

    def show_student(self):
        self.show_info()  # Reusing parent method
        print(f"Student ID: {self.student_id}")


# Object of Student class
s1 = Student("Arman", 21, "ST1234")
s1.show_student()
