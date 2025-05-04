def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"My name is {self.name}"

# Example usage
if __name__ == "__main__":
    person = Person("John")
    print(person.introduce())
    print(person.greet()) 