from rest_framework import serializers
from .models import Path, Student
from django.utils.timezone import now



#! Bu örnek serializers.Serializer örneğidir.Kod yazımı biraz fazladır!!
#-----------------------------------------------------------------

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     number = serializers.IntegerField()
#     # id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance


#! Bu örnek model.Serializer örneğidir.Kod yazımı azdır!!
#-----------------------------------------------------------------

class StudentSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields= ["number","first_name","last_name","id","register_date","days_since_joined"]
        # fields= "__all__"
        # exclude = ("last_name",) #tuple gösterimi
        # exclude = ["last_name"] #LİST gösterimi

    def validate_first_name(self, value):
        if value.lower()== 'rafe' :
            raise serializers.ValidationError("Rafe can not be our students!!")
        return value   

    def validate_number(self,value):
        if value>1000:
            raise serializers.ValidationError("The number must below 1000!")
        return value

    def get_days_since_joined(self, obj):
        return (now() - obj.register_date).days     #gün olarak gösterim şekli.
        #return (now() - obj.register_date).seconds #dakika oalrak gösterim şekli.


class PathSerializer(serializers.ModelSerializer):
    students =StudentSerializer(many=True) 
    #students = serializers.StringRelatedField(many=True)
    #students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Path
        fields = "__all__"

#* Yukarıda "nested-serializer" örneği yapıyoruz ve pathleri başlığı altında pathe seçili öğrencileri gösteriyoruz.
#! Eğer (many=True) tanımlaması yapmaz isek kayıtlı öğrencilerin birden fazla olduğu için göstermezdi.Yani bir pathe
#!tanımlı birden fazla öğrenci gösterebilmek için (many=True) yapmalıyız.!! 
#*1-)students =StudentSerializer(many=True) diyerek normal gösterimi sağlıyoruz.Yani path içindeki öğrencilerin tüm fieldları.
#*2-)students = serializers.StringRelatedField(many=True) diyerek modelda tanımladığımız "__str__" tanımlamasında yazılı field gösterilir
#*2-)yani def __str__(self): return self.first_name dersek yukarıdaki örnek için first_name gösterilir sadece !!!!
#*3-)students = serializers.PrimaryKeyRelatedField(read_only=True, many=True) diyerek primarykeyleri gösterebiliriz.!!


#                       ----------------NOT's----------------:
#! Serializer:Complex yapıların python veri yapılarına veya tam tersi işlemin gerçekleşmesini sağlar."json -->python" veya "python-->json" 
#* 2 şekilde serializers tanımlaması yapabiliriz.
#1-(serializer.Serializer) tanımlaması ile yukarıdaki örnek gibi fieldları tektek tanımlayabiliriz. (MANUEL)
#2-(serializer.ModelSerializer) tanımlaması ile hazır modelimizin fieldlarını direk seçebiliriz.İçlerinden istediğimizi ekranada
#yansıtabiliriz hepsinide yansıtabiliriz.!! (AUTO)
#! Yeni kayıt yapmak için (create func.) tanımlamalıyız.Update işlemi içinde (update func.) tanımlamalıyız.
#* Create işlemini "Post" ile Update işlemini "Put" ve "Patch" ile yapabiliriz.
# Put ve Patch arasındaki farka gelince:
# Tüm fieldlarda değişiklik yapmak istiyorsak put tercih edilir,Ancak tek bir fieldda yada kısmı değişiklik için patch kullanılır.

#*2.yöntem ModelSerializer tanımlamasında yazım daha basittir.Model="modelAdı" ve fieldsları yazıyoruz.
#!fieldsları 3 farklı yolla tanımlayabiliriz.
#1-)fields ='__all__' ile tamamını gösterebiliriz.
#2-)fields = ['field1','field2','field3'....] field isimlerini hepsini veya istediklerimizi yazarak gösterebiliriz.Yazılan sıraya göre gösterilir.
#3-)exclude = ["istemediğimiz fieldı yazıyoruz haricindekileri göster diyoruz."] **gösterim "list" veya "tuple" içerisinde olabilir.**

#* Fields larımıza validation yapabiliriz.Bunun için yukarıda örnek yaptım. Bir fonksiyon tanımlıyoruz ve
#! def validate_"field ismi" olarak tanımlıyoruz ve bir koşulla validationumuzu gerçekleştiriyoruz.
# örnekte first_name == rafe ise şu mesajı ver diyerek bir validation yaptım !!.
#! TÜM SATIRLAR İÇİN GENEL KURAL "INDENTATİON(GİRİNTİ)" ÖNEMLİ !!! :) 

#!modelsda tanımlı olmayan bir field'ı direk serializerda tanımlayabiliriz.Yukarıda örneğini yaptım.
#Bir func.ile days_since_joined adında fields tanımladık ve şuanki zaman-oluşturulma zamanı farkını aldık.
#Eğer fields gösterimlerinden "__all__" seçili değilse fields = kısmına yeni fieldsımızı eklemeyi unutmayalım.
#Örnekte farkı gün(days) olarak istedik.Ancak dakika(seconds) olarakta isteyebiliriz.

#!Serializers içinde serializers gösterimi yapabiliriz.Buna "nested-serializer" denir.
#*Yukarıdaki örnekte altında açıklamalar yaptım.Oraya bakabilirsin.!!