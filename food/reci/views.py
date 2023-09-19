from django.shortcuts import render,redirect
from .models import *

def receipes(request):

    if request.method == 'POST':
        data=request.POST
        recepie_name=data.get('recepie_name')
        recepie_image=request.FILES.get('recepie_image')
        receipe_description=data.get('receipe_description')
        
        Receipe.objects.create(
            recepie_name=recepie_name,
            recepie_image= recepie_image,
            receipe_description=receipe_description,
        )
        # s=Receipe(recepie_name=recepie_name,recepie_image= recepie_image,receipe_description=receipe_description,)
        # s.save()
           
        return redirect('/receipes/')
    queryset=Receipe.objects.all()
    context={'receipes':queryset}


    return render(request,'receipes.html',context)


def delete_recepie(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')

def update_recepie(request,id):
    queryset=Receipe.objects.get(id=id)
    context={'receipes':queryset}

    return render(request,'update_recepie.html',context)


