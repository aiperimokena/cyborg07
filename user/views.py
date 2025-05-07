import random

import ssl
import certifi
ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl._create_default_https_context = ssl_context

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import UserRegisterForm
from .models import OTP




def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have been registered!")
            return redirect('index')

        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{error}')

    form = UserRegisterForm()
    return render(request, 'account/user_register.html',{'form': form} )

#cndm zleo anve mxyw

def generate_otp_code():
    randome_code = random.randint(100000, 999999)
    return randome_code


def user_login_view(request):

    if request.method == "POST":
       user_email = request.POST['email']
       user_password = request.POST['password']

       user = authenticate(request, username=user_email, password=user_password)

       if user:
            otp = OTP(
               user=user,
               code=generate_otp_code()
           )
            otp.save()

            send_mail(
                "One time password for Cyborg07",
                f"Your OTP code is: {otp.code}",  # Make sure to include the actual OTP code
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
                fail_silently=False,
            )

            messages.success(request, "You have been loged in")
            return redirect('index')
       else:
            messages.error(request, "Wrong login or password")

    return render(request, 'account/user_login.html')

def user_logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('index')

