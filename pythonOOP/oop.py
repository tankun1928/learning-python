#Intro to OOP
class Car() :
    #init method or constructor
    def __init__(self, brand, model, year) :
        self.brand = brand
        self.model = model
        self.year = year
        
    def show_info(self) :
        print(self.brand + " " + self.model + " " + str(self.year))
    
        
myCar = Car("toyota","vios",2010)      # Object instantiation (object creation)
TomCar = Car("honda","civic", 2018)
JackCar = Car("suzuki","swift",2012)

myCar.show_info()
Car.show_info(TomCar)