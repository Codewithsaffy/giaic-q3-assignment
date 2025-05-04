class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"{cls.count} times object created from this class")


Counter()
Counter()
Counter()
Counter()
Counter.display_count() #it display 4 times