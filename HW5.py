class Car:
    def __init__(self, brand, _year, color):
        self.brand = brand
        self._year = _year
        self.color = color

    def roof(self):
        return "I'm convertible!"

    def set_year(self, year_for_another_car):
        self._year = year_for_another_car

car1 = Car('Ford', 2015, 'Blue')
car2 = Car('GMC', 2022, 'Silver')

class German(Car):
    def __init__(self, brand, _year, color, type_of_car):
        super().__init__(brand, _year, color)
        self.type_of_car = type_of_car

car3 = German('Audi', 2019, 'Yellow', 'Coupe')
car4 = German('Mercedes', 2020, 'White', 'Sedan')

print(car1.color)
print(car2.brand)
print(car1._year)
print(car2.__dict__)
print(car3._year)
print(car4.type_of_car)
print(car4.color)
print(car4.__dict__)
print(car4._year)