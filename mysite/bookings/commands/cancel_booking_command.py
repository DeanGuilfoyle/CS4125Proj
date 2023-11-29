# bookings/commands/cancel_booking_command.py

class CancelBookingCommand:
    def __init__(self, booking):
        self.booking = booking

    def execute(self):

        self.booking.delete()
