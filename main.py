def decorator(func):
    def wrapper(n):
        print("Fibonacci sonlari:")
        func(n)

    return wrapper


@decorator
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = int(input("n = "))
fibonacci(n)