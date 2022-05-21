from django import forms
from .models import Student

class StudentFormSimple(forms.Form): # Bu gösterimle manuel form oluşturulur ancak pratik kullanım değildir.
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    number = forms.IntegerField(required=False)

class StudentForm(forms.ModelForm):  # Bu şekilde hazır modellerden form kullanımı daha pratik yöntemdir.
    class Meta:
        model= Student
        fields= "__all__"  #Tüm fieldları ekrana yansıtmamızı sağlar.
        # fields= ["first_name","last_name"]   # Bu şekilde kullanırsak sadece first ve last name yazdırılır.
        labels= {"last_name":"Surname"} # İsim değişikliği yapmak istersek kullanılır.