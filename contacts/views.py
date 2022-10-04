from django.shortcuts import render, redirect
from . models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_inquiry = request.POST['customer_inquiry']
        city = request.POST['city']
        county = request.POST['county']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already inquired about this car, please wait until we get back to you')
                return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_inquiry=customer_inquiry, city=city, county=county, email=email, phone=phone, message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email  = admin_info.email
        send_mail(
            'Website Car Inquiry',
            'You have a new inquiry for the car, Please login to your admin panel for more info.',
            'micmojainc@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        contact.save()

        # Send success message to the customer_inquiry
        messages.success(request, 'Your request has been submitted successfully, A representative of Planet Motors will get back to you shortly.')
        return redirect('/cars/'+car_id)
