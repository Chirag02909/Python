class Car:
    total_car = 0

    def __init__(self , brand , model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def fullname(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla" , "Model S" , "85kwh")

# print(isinstance(my_tesla , Car))
# print(isinstance(my_tesla , ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.fullname())
# print(my_tesla.fuel_type())

# my_Car = Car("TATA" , "Safari")
# print(my_Car.fuel_type())
# print(my_Car.brand)
# print(my_Car.model)
# print(my_Car.fullname())
# print(my_Car.general_description())
# print(Car.general_description())

# new_car = Car("SUZUKI" , "Swift")
# print("\n"+new_car.brand)
# print(new_car.model)
# print(new_car.fullname())

# print(Car.total_car)



class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"


class ElectricCarTwo(Battery ,Engine, Car):
    pass

mynew_tesla = ElectricCarTwo("Tesla" , "Model S")
print(mynew_tesla.engine_info())
print(mynew_tesla.battery_info())