from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def UserForm(request):
    finalans=0
    context={}
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            context={
               'n1':n1,
               'n2':n2,
               'output':finalans
            }
            url=f"/home/?output={finalans}"
            # return HttpResponseRedirect('/home/')
            # return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass

    return render(request,'UserForm.html',context)


def home(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,'home.html',{'output':output})