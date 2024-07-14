from django.shortcuts import render, redirect

from newApp.forms import StudentForm
from newApp.models import Student


# Create your views here.
def home(request):
    return render(request, 'home.html')
def service(request):
    return render(request, 'service.html')
def index(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request,'index2.html')
def dashboard2(request):
    return render(request,'index3.html')
#Create
def students(request):
    data=StudentForm()
    if request.method == 'POST':
        data1 = StudentForm(request.POST)
        if data1.is_valid():
            data1.save()
    return render(request,'home.html',{'form':data})

#Read
def student_list(request):
    data=Student.objects.all()
    return render(request,'list.html',{'data':data})

#update
def update(request,id):
    todo=Student.objects.get(id=id)
    form = StudentForm(instance=todo)
    if request.method == 'POST':
        form=StudentForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request,'update.html',{'form':form})

#delete
def delete(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect('student_list')
