from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    todo_detail = serializers.HyperlinkedIdentityField(view_name="todo-detail")
    #!browserda detail sayfasına kolay ulaşım için link oluşturur. 

    class Meta:
        model= Todo
        #fields="__all__"
        fields = ("id","task","description","priority","done","todo_detail")
        #!Fieldslarımızı bu şekilde tanımlamamızın sebebi yukarıda tanımladığımız todo_detail'i kullanabilmek için.
        #!todo_detail bize browserda todolarımızı gösterirken yanlarına detail sayfalarına ulaşmak için otomatik link oluşturuyor.
        
        