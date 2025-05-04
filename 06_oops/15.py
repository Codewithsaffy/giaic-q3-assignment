class A:
    def show(self):
        print("This is class A")

class B(A):
    def show(self):
        print("This is class B")
        super().show()

class C(A):
    def show(self):
        print("This is class C")
        super().show()

class D(B, C):
    def show(self):
        print("This is class D")
        super().show()

# Example usage
if __name__ == "__main__":
    # Create object of class D
    d = D()
    
    # Call show() method
    print("Calling show() method:")
    d.show()
    
    # Print MRO
    print("\nMethod Resolution Order (MRO):")
    print(D.__mro__) 