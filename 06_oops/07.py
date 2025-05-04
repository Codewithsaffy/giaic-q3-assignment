class Employee :
    def __init__(self, name , salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn= ssn


one = Employee("yousuf", 1000, 12)
print(one.name)
print(one._salary) # it is not allowed but we can access it 
print(one.__ssn) # it give error 