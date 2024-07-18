

class Car: 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 

    def get_descriptive_name(self): 
        print(f"{self.year}-{self.make}-{self.model}") 


class Battery: 
    def __init__(self, battery_size): 
          self.battery_size = battery_size

    def describe_battery(self): 
        print(f"This car has a {self.battery_size} kWh battery") 

class ElectricCar(Car): 
    def __init__(self, make, model, year): 
        super().__init__(make, model, year) 
        self.battery = Battery("75") 



audi = Car("Audi", "a8", "2015") 


electricCar = ElectricCar("tesla", "model s", 2019)
battery = electricCar.battery.battery_size
print(battery)
 
