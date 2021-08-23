from django.shortcuts import render, redirect

from bank_sys.settings import BASE_DIR

from .models import AmortizationTablesForBank, RequiredLoan
from django.http import HttpResponse


# Create your views here.


def home(request):
    atfb = AmortizationTablesForBank.objects.all()
    requiredloans = RequiredLoan.objects.all()
    return render(request, "home.html", {'home': requiredloans})


# def profile(request,user_id):
#     form = ProfileForm()
#     return render(request, '')

# def add_new_user(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('last_name')
#             email = form.cleaned_data.get('email')
#             balance = form.cleaned_data.get('balance')
#             type = form.cleaned_data.get('type')
#             return redirect('home')
#         else:
#             form = SignupForm()
#         return render(request, 'add_new_user.html', {'form': form})
