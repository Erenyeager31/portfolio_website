from django.shortcuts import render,HttpResponse
from myportfolio.models import project

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def Project(request):
    p = project()
    list = project.objects.values()
    print(list)

    return render(request,'project.html',{'p_list':list})