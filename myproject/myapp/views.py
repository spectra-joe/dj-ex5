# authentication/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            request.session['username'] = form.cleaned_data['username']
            request.session['email'] = form.cleaned_data['email']

            response = HttpResponse("Session created successfully and cookie set!")

            response.set_cookie('username', form.cleaned_data['username'])
            response.set_cookie('email', form.cleaned_data['email'], max_age=3600)

            print(f"Session username: {request.session.get('username')}")
            print(f"Session email: {request.session.get('email')}")

            return response
    else:
        form = LoginForm()

    return render(request, 'myapp/login.html', {'form': form})