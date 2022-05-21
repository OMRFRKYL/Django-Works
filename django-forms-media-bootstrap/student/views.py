from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import StudentForm
from django.contrib import messages

def index(request):
    return render(request, 'student/index.html')

def student_page(request):

    form = StudentForm(request.POST or None)
    if form.is_valid(): # formisvalid() backende boş field gönderilmemesi için kontrol mekanızmasıdır.
       student = form.save()
       if "profile_pic" in request.FILES:
           student.profile_pic = request.FILES["profile_pic"]
           student.save()
       messages.success(request,"Student saved successfully")
       return redirect("student") 
       #Redirect Formun içerisini boşaltmak için ve butona basıldığında index sayfasına yönlendirme için kullanılır.
       
       # print(form.cleaned_data.get("first_name"))
    context={
        "form":form
    }
    return render(request,'student/student.html',context)