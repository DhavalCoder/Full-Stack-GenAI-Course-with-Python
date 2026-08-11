from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Befor Function runs")
        func()
        print("After function runs")
    return wrapper


@my_decorator
def greet():
    print("Hello from decorators from Dhaval!")

greet()    
print(greet.__name__)