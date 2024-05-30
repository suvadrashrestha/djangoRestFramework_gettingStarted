from django.urls import path
from . import views
urlpatterns=[
    path('list/',views.car_list_view,name="car_list"),
     #  <> =  capture a part of the URL and pass it as a parameter to a view function.
    path('<int:pk>/',views.car_detail_view,name="car_detail"),
    #as_view routes the http method like get,post etc to its corresponding get,post method defined in view .
    path('showroom/',views.ShowroomView.as_view(),name="showroom"),
    path('showroom/<int:pk>/',views.ShowroomDetailView.as_view(),name="showroom_detail"),
]