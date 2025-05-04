class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result

# Example usage
if __name__ == "__main__":
    # Create countdown from 5
    countdown = Countdown(5)
    
    # Using for loop
    print("Countdown using for loop:")
    for number in countdown:
        print(number)
    
    # Create another countdown
    countdown2 = Countdown(3)
    
    # Using next() function
    print("\nCountdown using next():")
    print(next(countdown2))
    print(next(countdown2))
    print(next(countdown2))
    print(next(countdown2))
    
    # This will raise StopIteration
    try:
        print(next(countdown2))
    except StopIteration:
        print("Countdown finished!") 