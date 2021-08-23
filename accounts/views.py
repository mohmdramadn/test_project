from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignupForm


# Create your views here.


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            # email = form.cleaned_data.get('email')
            # balance = form.cleaned_data.get('balance')
            # type = form.cleaned_data.get('type')
            return redirect('home')

    return render(request, "signup.html", {'form': form})
