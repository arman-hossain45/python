
#Create a class Car with attributes like brand, model, and year. Write a method to display the car’s details.

# class car:
#     def __init__ (self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year

#     def info(self):
#         print(f"car detais is {self.brand},brand model is {self.model}, and year is {self.year}")

# value=car("x_corolla","fb23","2014")
# value.info()


#Define a class Student with attributes name, roll, and marks. Write a method to check if the student has passed (marks ≥ 40)
class student:
    def __init__ (self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def info(self):
        if self.marks>40:
            print(f"The name of the student {self.name}\n Roll is {self.roll}\n PASS")

        else:
              print(f"The name of the student {self.name}\n Roll is {self.roll}\n FAIL")


value=student("Arman",231061008,90)
value.info()