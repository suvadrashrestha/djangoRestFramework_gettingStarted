from rest_framework import serializers

from .models import CarList,ShowroomList

def alphanumneric(value):
     if not str(value).isalnum():
          raise serializers.ValidationError("only  alphanumeric is allowed")


class showroomSerializer(serializers.ModelSerializer):

     class Meta:
          model=ShowroomList
          fields='__all__'





class CarSerializer(serializers.ModelSerializer):
#     This is for serializers.Serializer class
#     #the name of attribute must be same as model attribute for serializer class
#     price=serializers.DecimalField(max_digits=9,decimal_places=2)
#     cassinumber=serializers.CharField(validators=[alphanumneric])
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     description=serializers.CharField(required=False,allow_blank=True)
#     active=serializers.BooleanField(read_only=True)



# This is for serializer.ModelSerializer class
    # get must be added in the method of this attribute
    discounted_price=serializers.SerializerMethodField()


    class Meta:
         model=CarList
     #     fields='__all__'
         exclude=['active']

    
    def get_discounted_price(self,object):
         discount= object.price-100
         return discount
     
    def validate_price(self,data):
         if data<=2000:
              raise serializers.ValidationError("the price cannot be less than 2000")
         return data
    
    def validate(self, attrs):
         if attrs['name']==attrs['description']:
              raise serializers.ValidationError("name and description cannot be same")
         return attrs

    def create(request,validate_data):
         return CarList.objects.create(**validate_data)
    
    def update(request,instance,validated_data):
         instance.name=validated_data.get("name",instance.name)
         instance.description=validated_data.get("description",instance.description)
         instance.active=validated_data.get("active",instance.active)
         instance.save()
         return instance
    
