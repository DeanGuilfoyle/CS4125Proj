# decorator interface
class PricingDecorator:
    def __init__(self, car):
        self.car = car

    def calculate_price(self, price):
        pass

# concrete decorators
class InsuranceDecorator(PricingDecorator):
    def calculate_price(self, price):
        return price + 15  # Add insurance cost

        