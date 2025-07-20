from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"DoB: {self.dob}")
    
    @abstractmethod
    def work(self):
        pass

class Employee(Person):
    def __init__(self, name, id, dob, rate):
        super().__init__(name, id, dob)
        self.rate = rate

    def calc_salary(self, hours):
        return hours * self.rate
    
    def display_info(self):
        super().display_info()
        print(f"Rate: {self.rate}")

    def work(self):
        print("Working")
    
class Student(Person):
    def __init__(self, name, id, dob, cgpa):
        super().__init__(name, id, dob)
        self.cgpa = cgpa

    def calc_cgpa(self):
        return self.cgpa
    
    def display_info(self):
        super().display_info()
        print(f"CGPA: {self.cgpa}")
    
    def work(self):
        print("Working")

if __name__ == "__main__":
    e = Employee("Tauseef", "109", "6/7/24", 200)
    s = Student("Tajwar", "110", "6/7/24", 0.0)
    e.display_info()
    