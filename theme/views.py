from django.shortcuts import render
from catering.models import Product
def home(request):
    return render(request, 'theme/home.html')
