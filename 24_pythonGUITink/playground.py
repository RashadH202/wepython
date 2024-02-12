
# @args: Positional Variable length arguments
def add(*args):
    return sum(args)

# **kwargs: Keyworded Variable_length Arguments
def calculate(n , ** kwargs):
    n += kwargs.get("add", 0)
    n *= kwargs.get("multiply", 1)
    print(n)

calculate(2, add=3, multiply=5)

#using **kwargs in a class constructor
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
