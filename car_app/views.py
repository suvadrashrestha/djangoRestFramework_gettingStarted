from django.shortcuts import render
from .models import CarList,ShowroomList
from .serializers import CarSerializer,showroomSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.



#converting complex data into json without serializer
# import json
# from django.http import JsonResponse,HttpResponse
# def car_list_view(request):
#     cars=CarList.objects.all()
#     data={
#         'cars':list(cars.values())
#     }
#     response=json.dumps(data)
#     return HttpResponse(response,content_type="application/json")
#     # return JsonResponse(data)

# def car_detail_view(request,pk):
#     car=CarList.objects.get(pk=pk)
#     data={
#        "name":car.name,
#        "decription":car.description,
#        "active":car.active
#     }
#     return JsonResponse(data)
    



# function based view
@api_view(['GET','POST'])
def car_list_view(request):
    if request.method=='GET':
        car=CarList.objects.all()
        serializer=CarSerializer(car,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=CarSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

           
@api_view(['GET','PUT','DELETE'])
def car_detail_view(request,pk):
    if request.method=="GET":
        try:
            car=CarList.objects.get(pk=pk)
        except :
            return Response({"error":"car doenot exist"},status=status.HTTP_404_NOT_FOUND)
        serializer=CarSerializer(car)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        car=CarList.objects.get(pk=pk)
        #weather to create or update depends if you pass instance or not 
        serializer=CarSerializer(car,data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        car=CarList.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class based view with  extending APIview class 
class showroomView(APIView):
    def get(self,request):
        showroom=ShowroomList.objects.all()
        serializer=showroomSerializer(showroom,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=showroomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data,status=status.HTTP_201_CREATED)
        





