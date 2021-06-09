from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="UserHome"),
    path('Contact', views.Contact, name="Contact"),
    path('User_Notifications',views.User_Notifications,name="User_Notifications"),
    path('Pregnancy',views.Pregnancy,name="Pregnancy"),
    path('Palliative',views.Palliative,name="Palliative"),

]