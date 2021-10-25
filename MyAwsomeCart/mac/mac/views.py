from django.shortcuts import render
# project views i have Created 
# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')