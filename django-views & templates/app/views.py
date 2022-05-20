from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # print(request.method)  #requestimizin methodunu bize verir.Bu örnek için GET methodu.
    # print(request.COOKIES)  #DJANGO frameworkü için güvenlik ayarlarını içerir.
    #print(request.user)  #Login olmuş olan user'ı gösterir.Bu örnek için anonymousUser.
    #print(request.path)  #Hangi domainde olduğumuzu gösterir.
    print(request.META) #reuest ile gelen metadataları gösterir.
    return HttpResponse("<h1>Hello World!</h1>")

def special(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render (request,"app/special.html",context)
#NOT:app altına templates/app klasörü oluşturucaz ve altına special.html dosyası oluşturmamız gerekiyor.