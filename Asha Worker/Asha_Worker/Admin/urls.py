from django.urls import path
from . import views
urlpatterns = [
    path('', views.AdminHome, name="AdminHome"),
    path('Add_Organizer', views.Organizer, name="Organizer"),
    path('Add_Location', views.Location, name="Location"),
    path('Reports', views.Reports, name="Reports"),
    path('state-json/', views.get_json_state, name="state-json"),
    path('district-json/<str:state>/', views.get_json_district, name="district-json"),
    path('Logout', views.Logout, name="Logout"),

]