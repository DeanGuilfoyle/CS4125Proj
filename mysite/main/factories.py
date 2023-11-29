from .models import Sedan, Coupe

class CarFactory:
    def create_car(self):
        pass


# concrete factories that inherit from CarFactory
class SedanFactory(CarFactory):
    def create_car(self):
        return Sedan()

class CoupeFactory(CarFactory):
    def create_car(self):
        return Coupe()
