class Laptop:
    def __init__(self,brand,age):
        self.brand = brand
        self.age = age
    def increase_age(self,age=1):
        self.age += age
    def repair (self,lifeIncrease):
        self.increase_age(lifeIncrease)
my_laptop = Laptop('Toshiba',2)
my_laptop.increase_age(2)
print(my_laptop.age)
my_laptop.age = 14
my_laptop.increase_age(3)
print(my_laptop.age)
my_laptop.repair(-5)
print(my_laptop.age)
print(my_laptop.__dict__)
