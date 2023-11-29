class BookingInvoker:
    def __init__(self):
        self.history = []

    def execute(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            command = self.history.pop()
            # You can implement an undo operation for the specific command if needed
            # For example, if you need to undo a booking, you might want to implement
            # logic to cancel the booking.

            # command.undo()  # Implement the undo logic in your commands if required
