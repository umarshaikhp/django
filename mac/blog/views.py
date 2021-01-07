from django.shortcuts import render
#i have created the views
# Create your views here.
from  django.http import HttpResponse
def index(request):
    return render(request,'blog/index.html')



