class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subjet = subject

first  = Teacher("yousuf", subject="math")
print(first.name, first.subjet)
