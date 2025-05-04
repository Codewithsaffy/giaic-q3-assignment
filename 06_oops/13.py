# Engine class
class Engine:
    def start(self):
        print("Engine started!")

# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composed Engine object

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Calling Engine's method via Car

# Create an Engine object
engine = Engine()

# Pass Engine object to Car
my_car = Car(engine)

# Use Car's method which uses Engine's method
my_car.start_car()
