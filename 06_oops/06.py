class Logger:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} object created")

    def __del__(self):
        print(f"{self.name} Object destroyed")


obj = Logger("check")

del obj