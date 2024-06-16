class Vehicle:
    vehicle_type = "none"

    def __init__(self, mode, powers):
        self.mode = mode
        super().__init__(powers)


class Car:
    price = 1000000

    def __init__(self, powers):
        self.powers = powers
        self.vehicle_type = "Car"

    def horse_powers(self):
        return self.powers


class Nissan(Vehicle, Car):
    def __init__(self, mode, price, powers):
        super().__init__(mode, powers)
        self.price = int(price)


nissan_1 = Nissan("Patrul", 2000, 210)
#print(nissan_1.__dict__)
#print(dir(nissan_1))
print(f"Тир транспортного средства : {nissan_1.vehicle_type} ")
print(f"Стоимость :{nissan_1.price}")
print(f"Мощность :{nissan_1.horse_powers()}")
