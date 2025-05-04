class Student():
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    def display(self):
        print(f"{self.name} score {self.mark}")


yousuf = Student("yousuf", 100)
yousuf.display()