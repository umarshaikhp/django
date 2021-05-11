#i have created file views :umar

from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request,'index.html')


def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    print(djtext)
    punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed=""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if (fullcaps == "on"):
        analyzed = ""
        print("welcome")

        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover=="on"):
        analyzed=""

        for char in djtext:
            if char!="\n" and  char!="\r":
                # print(char)
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""

        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'extraspaceremover', 'analyzed_text': analyzed}
        djtext=analyzed

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return render(request,'analyze2.html')

    return render(request, 'analyze.html', params)






