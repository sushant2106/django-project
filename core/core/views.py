from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def UserForm(request):
    finalans=0;
    try:
        n1=int(request.GET['num1'])
        n2=int(request.GET['num2'])

        # n1=request.GET.get('num1')
        print(n1+n2)
        finalans=n1+n2
    
    except:
        pass
    



    return render(request,'UserForm.html',{'output':finalans})
  