class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
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


class Teacher(Person):
    def introduce(self):
        last_name = self.name.split()[-1]
        print(f"Hello, I am Professor {last_name}, and I am {self.age} years old.")


# Example of creating and using methods of objects
p1 = Person("Jimmy O Yang", 37)

s1 = Student("Jason Kim", 10)
s2 = Student("Mason Ho", 15)
s3 = Student("Dason Li", 21)

t1 = Teacher("Matthew Poon", 30)
t2 = Teacher("Les Peters", 31)

p1.introduce()  # person

s1.introduce()  # elementary
s2.introduce()  # secondary
s3.introduce()  # university

t1.introduce()  # Professor Poon
t2.introduce()  # Professor Peters

# Polymorphism
# people = [p1, s1, s2, s3, t1, t2]
#
# for person in people:
#     person.introduce()

# will yield the same result
