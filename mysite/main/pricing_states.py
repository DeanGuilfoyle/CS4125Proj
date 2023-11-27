class PricingState:
    def calculate_price(self, days, price):
        pass

class RegularPricingState(PricingState):
    def calculate_price(self, price):
        return price  # Regular price per day

class WeekendPricingState(PricingState):
    def calculate_price(self, price):
        return round(float(price) * 1.1, 2)  # Weekend price per day + 10%

class PromotionPricingState(PricingState):
    def calculate_price(self, price):
        return round(float(price) * .9, 2)  # Promotion price per day - 10%