#i have created file :umar

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)

    print(djtext)
    punctuations=''' !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    analyzed=""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

       # analyzed=djtext
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        #analyze the text
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def spaceremove(request):
#     return HttpResponse("remove space<a href='/'>back</a>")
#
# def newlineremove(request):
#     return HttpResponse("spaceremove")
#
# def charcount(request):
#     return HttpResponse("charcount")
