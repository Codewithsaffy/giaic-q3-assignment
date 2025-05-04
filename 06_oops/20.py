class InvalidAgeError(Exception):
    """Custom exception for invalid age values"""
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    return "Age is valid"

# Example usage
if __name__ == "__main__":
    # Test with valid age
    try:
        result = check_age(20)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}")
    
    # Test with invalid age
    try:
        result = check_age(15)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}")
    
    # Test with another invalid age
    try:
        result = check_age(-5)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}") 