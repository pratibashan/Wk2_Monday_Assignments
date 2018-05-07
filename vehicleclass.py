
class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self): 
        print(f"{self.year} {self.make} {self.model}") 



car = Vehicle('Nissan','Leaf','2015')
print(car.make)
print (car.model)
print (car.year)          
car.print_info()