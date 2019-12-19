from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, PhoneForm, CodeForm
import random, string
from .models import Phone
import requests


def verify(request):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            phoneObj = Phone(number=form.cleaned_data['number'])
            phoneObj.code = code
            phoneObj.save()
            phoneNumber = phoneObj.number
            data = {
                'phoneNumber': phoneNumber,
                'message': f'Your confirmation code: {code}'
            }
            resp = requests.post('https://1d5za5biw2.execute-api.us-east-1.amazonaws.com/myStage/userinfo', json=data, headers={'Content-type': 'application/json'})
            print(resp)
            return redirect('confirm')
    else:
        form = PhoneForm
    return render(request, 'users/verify.html', {'form': form})


def confirm(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            trueCode = Phone.objects.last().code
            if code == trueCode:
                messages.success(request, 'You verified your account. You can login now!')
                return redirect('login')
            else:
                messages.warning(request, 'Wrong code, please try again!')
    else:
        form = CodeForm
    return render(request, 'users/confirm.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request, f'Your account has been created! You need to verify it!')
            return redirect('verify')
    else:
        form = UserRegisterForm
    return render(request, 'users/register.html', {'form': form})
