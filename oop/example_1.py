class Person:
    def __init__(self, name, age):
        # self refers to the object that is created with this class
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


# object called "my_teacher" is created
my_teacher = Person("Poon", 32)

# my_teacher uses a method called "introduce()"
my_teacher.introduce()

# my_teacher's property of "name" is accessed
print(f"My teacher's name is Mr. {my_teacher.name}")
