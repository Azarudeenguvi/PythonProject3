class vehicle:
    def __init__(self,model,rentrate,hour):
        self.model=model
        self.rentrate=rentrate
        self.hour = hour
    def calculate_rent(self):
        print(f'vehicle type : {self.model}  cost : {self.rentrate}')

class Car(vehicle):
    def calculate_rent(self):
        print(f'vehicle type : {self.model}  cost : {self.rentrate*self.hour}')

class Bike(vehicle):
    def calculate_rent(self):
        print(f'vehicle type : {self.model}  cost : {self.rentrate*self.hour}')

class Truck(vehicle):

    def calculate_rent(self):
        print(f'vehicle type : {self.model}  cost : {self.rentrate*self.hour}')

c=[Car('punto',25,5),Bike('pulse125',10,3),Truck('Eicher',100,5)]
for i in c:
    i.calculate_rent()