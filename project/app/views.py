from multiprocessing import context
from django.shortcuts import render,HttpResponse
from . models import Contact
def index(request):
    if request.method == 'POST':
        name= request.POST["name"]
        email=request.POST["email"]
        ship=request.POST["ship"]
        pro=request.POST["pro"]
        context = Contact(name=name,email=email,ship=ship,pro=pro)
        context.save()
    return render(request,'app/index.html')
    

# Create your views here.
