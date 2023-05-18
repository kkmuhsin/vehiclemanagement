from vehicle import views
from django.urls import path,include
app_name='vehicle'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('',views.home,name='home'),
    path('details/',views.details,name='details'),
    path('vehicledetails/',views.vehicledetails,name='vehicledetails'),
    path('update/<int:pk>',views.update,name='update'),


]