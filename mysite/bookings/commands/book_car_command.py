from bookings.models import Booking

class BookCarCommand:
    def __init__(self, car, user, start_date, end_date, total_price):
        self.car = car
        self.user = user
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = total_price

    def execute(self):
        # Create a Booking instance and save it
        booking = Booking(
            car=self.car,
            user=self.user,
            start_date=self.start_date,
            end_date=self.end_date,
            total_price=self.total_price
        )
        booking.save()