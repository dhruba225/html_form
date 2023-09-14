from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_school(request):
    if request.method=='POST':
        scn=request.POST['scn']
        sch=request.POST['sch']
        scl=request.POST['scl']

        so=School.objects.get_or_create(ScName=scn,ScHead=sch,ScLoc=scl)[0]
        so.save()
        QLSO=School.objects.all()
        d={'QLSO':QLSO}
        return render(request,'display_school.html',d)
        
    return render(request,'insert_school.html')