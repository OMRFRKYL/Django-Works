from django.db import models
#!ONE TO ONE EXERCİSES
class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
 
    def __str__(self):
        return self.first_name

class Language(models.Model):
    name = models.CharField(max_length=50)
    creator = models.OneToOneField(Creator,on_delete=models.CASCADE)
    #creatoru burada onetoone ile oluşturduk ve creator tablosuyla bağlamış olduk.

    def __str__(self):
        return self.name

#!MANY TO ONE EXERCİSES:

class Frameworks(models.Model):
    name=models.CharField(max_length=40)
    language = models.ForeignKey(Language,on_delete=models.PROTECT)

    def __str__(self):
        return self.name

#!MANY TO MANY EXERCİSES:

class Developers(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    frameworks=models.ManyToManyField(Frameworks) #one_delete vermeye gerek yok çünkü birden fazla etkileşim mevcut.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


#! one_delete Methodları:
#! CASCADE  - parent silinince silinir.
#! SET_NULL  - parent silinince null yapar.
#! PROTECT   - parent silinince hata verir.
#! DO_NOTHING - parent silinince hiçbir şey yapmaz.
#! SET_DEFAULT - parent silinince default değer atar.