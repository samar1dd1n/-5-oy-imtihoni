# def decorator(func):
#     def wrapper(n):
#         print("Fibonacci sonlari:")
#         func(n)
#
#     return wrapper
#
#
# @decorator
# def fibonacci(n):
#     a, b = 0, 1
#
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
#
#
# n = int(input("n = "))
# fibonacci(n)

#2- masala
# def decorator(func):
#     def wrapper(a):
#         func(a)
#
#         b = []
#         summa = 0
#
#         for i in a:
#             summa += i
#             b.append(summa)
#
#         print("B massiv:", b)
#
#     return wrapper
#
#
# @decorator
# def massiv(a):
#     print("A massiv:", a)
#
#
# n = 5
# a = [2, 3, 5, 8, 9]
#
# massiv(a)

#3- masala
from collections import namedtuple

Car = namedtuple("Car", ["brand", "model", "year", "mileage"])

cars = []

for i in range(5):
    print(f"{i + 1}-mashina")
    brand = input("Brend ")
    model = input("Model")
    year = input("Yili ")
    mileage = int(input("Yurgan masofasi "))

    cars.append(Car(brand, model, year, mileage))

min_car = min(cars, key=lambda car: car.mileage)

print("\neng kam yurgan mashina")
print(f"Brend: {min_car.brand}")
print(f"Yurgan masofasi: {min_car.mileage}")