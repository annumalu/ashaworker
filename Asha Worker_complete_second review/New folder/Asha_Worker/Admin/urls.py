from django.urls import path
from . import views

urlpatterns = [
    path('',views.AdminHome,name="AdminHome"),
    path('Add_Organizer',views.Organizer,name="Organizer"),
    path('Add_Location',views.Location,name="Location"),
    path('Reports',views.Reports,name="Reports"),
    path('Logout',views.Logout,name="Logout"),
    path('state-json/',views.get_json_state,name="state-json"),
    path('district-json/<str:state>/',views.get_json_district,name="district-json"),
    path('ward-state-json/',views.get_ward_state_json,name="ward-state-json"),
    path('ward-district-json/<str:state>/',views.get_ward_json_district,name="ward-district-json"),
    path('ward-pan-json/<str:dist>/',views.get_ward_json_pan,name="ward-pan-json"),
]