# bookings/views.py
from django.shortcuts import render, redirect
from .forms import BookingForm, CreditCardForm
from .models import Booking, Car  
from datetime import datetime, timedelta
from .commands.book_car_command import BookCarCommand
from .commands.cancel_booking_command import CancelBookingCommand
from .commands.booking_invoker import BookingInvoker
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def book_car(request, car_id):
    car = Car.objects.get(id=car_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            num_days = int(form.cleaned_data['days'])
            start_date = datetime.now().date()
            end_date = start_date + timedelta(days=num_days)

            # Calculate the total price
            car_price = car.price_per_day
            total_price = num_days * car_price

            # Create a booking command and execute it
            booking_command = BookCarCommand(car=car, user=request.user, start_date=start_date, end_date=end_date, total_price=total_price)
            booking_invoker = BookingInvoker()
            booking_invoker.execute(booking_command)

            if request.method == 'POST':
                credit_card_form = CreditCardForm(request.POST)
                if credit_card_form.is_valid():
                    # Simulate payment success or failure

                    return render(request, 'bookings/booking_success.html', {'car': car, 'total_price': total_price})
    else:
        form = BookingForm()

    return render(request, 'bookings/book_car.html', {'car': car, 'form': form})



@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = Booking.objects.get(id=booking_id)
        
        # Create a cancellation command and execute it
        cancellation_command = CancelBookingCommand(booking=booking)
        booking_invoker = BookingInvoker()
        booking_invoker.execute(cancellation_command)

        return redirect('view-bookings')  # Redirect to the same page to refresh the booking list
    
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})

def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)

    # Create a cancellation command and execute it
    cancellation_command = CancelBookingCommand(booking=booking)
    booking_invoker = BookingInvoker()
    booking_invoker.execute(cancellation_command)

    return redirect('car-list')

@staff_member_required
def view_all_bookings(request):
    bookings = Booking.objects.all()
    
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = Booking.objects.get(id=booking_id)
        
        # Create a cancellation command and execute it
        cancellation_command = CancelBookingCommand(booking=booking)
        booking_invoker = BookingInvoker()
        booking_invoker.execute(cancellation_command)

        return redirect('view-all-bookings')  # Redirect to the same page to refresh the booking list
    
    return render(request, 'bookings/view_all_bookings.html', {'bookings': bookings})


def booking_success(request):
    # You can add any additional logic here if needed
    return render(request, 'bookings/booking_success.html')