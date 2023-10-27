from typing import Callable

def my_decorator(func: Callable[[int], None]) -> Callable[[int], None]:
    def wrapper(num1: int) -> None:
        print("Something is happening before the function is called.")
        func(num1)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(num1: int) -> None:
    print(num1)

say_hello(100)
