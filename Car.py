class Car:
    def __init__(self, year_model, make, speed):
        self.year_model = year_model
        self.make = make
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

car1 = Car("2007 Toyota RAV$", "Hybrid", 0)
car2 = Car("2023 Ford F150", "Heavy Duty", 0)
print(car2.year_model)
for x in range(5):
    car2.accelerate()
    Ford_speed = car2.get_speed()
    print("Current speed:", Ford_speed)
for x in range(5):
    car2.brake()
    Ford_speed = car2.get_speed()
    print("Current speed:", Ford_speed)
# Program #2, Donovan Thompson 4/3/2025
