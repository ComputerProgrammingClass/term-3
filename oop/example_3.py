import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

        self.student_id = random.randint(10000, 20000)

    def introduce(self):
        level = self.get_school_level()
        print(f"Hi, I'm {self.name}, I'm {self.age}, and I'm in {level} school.")

    def get_school_level(self):
        if self.age < 13:
            return "elementary"
        elif self.age < 18:
            return "secondary"
        else:
            return "university"


s = Student("Lason Mu", 12)
s.introduce()
print(s.student_id)
