class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

# Example usage
if __name__ == "__main__":
    # Create multiplier objects
    double = Multiplier(2)
    triple = Multiplier(3)
    
    # Check if objects are callable
    print(f"Is double callable? {callable(double)}")
    print(f"Is triple callable? {callable(triple)}")
    
    # Use objects as functions
    print(f"Double of 5: {double(5)}")
    print(f"Triple of 5: {triple(5)}")
    
    # Test with different numbers
    numbers = [1, 2, 3, 4, 5]
    print("\nDoubling numbers:", [double(n) for n in numbers])
    print("Tripling numbers:", [triple(n) for n in numbers]) 