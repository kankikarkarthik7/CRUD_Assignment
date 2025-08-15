from django.urls import path, include
from . import views
from . import forms


appname = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/', views.details, name='details'),
     path('update/<int:pk>/', views.update_data, name='update_data'),
    path('delete/<int:pk>/', views.delete_data, name='delete_data'),
    path('contactus/',views.contactus, name='contactus')
    
]