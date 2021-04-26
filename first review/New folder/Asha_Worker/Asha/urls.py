from django.urls import path
from . import views

urlpatterns = [
    path('',views.AshaHome,name="AshaHome"),
    path('Profile/', views.Profile, name="Profile"),
    path('Download/', views.Download, name="Download"),
    path('Forms_View/', views.Forms_View, name="Forms"),
    path('Profile/get-state/',views.get_state,name="get-state"),
    path('Profile/district-json/<str:state>/',views.get_district,name="district-json"),
    path('Profile/ward-pan-json/<str:dist>/',views.get_pan,name="ward-pan-json"),
    path('Profile/ward-ward-json/<str:dist>/',views.get_ward,name="ward-ward-json"),
    path('Logout',views.Logout,name="Logout"),
]