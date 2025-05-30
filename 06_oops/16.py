def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    say_hello("John") 