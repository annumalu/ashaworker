from django.urls import path
from . import views

urlpatterns = [
    path('',views.AshaHome,name="AshaHome"),
    path('Profile/', views.Profile, name="Profile"),
    path('Download/', views.Download, name="Download"),
    path('Forms_View/', views.Forms_View, name="Forms"),
    path('Profile_Home', views.Profile_Home, name="Profile_Home"),
    path('Family_Register/', views.Family, name="Family"),
    path('UpdateFamily/', views.updateFamily, name="updateFamily"),
    path('Baby_Register/', views.Baby_Register, name="Baby"),
    path('Main_Home/', views.Main_Home, name="Main_Home"),
    path('UpdateProfile/', views.updateprofile, name="updateprofile"),
    path('deleteprofile/', views.deleteprofile, name="deleteprofile"),
    path('Search/',views.Search,name='Search'),
    path('Advancedsearch/',views.Advancedsearch,name='Advancedsearch'),
    path('Report/',views.Report,name='Report'),
    path('Contact_User/', views.Contact_User, name="Contact_User"),
    path('Notifications_View/', views.Notifications_View, name="Notifications"),
    path('User_Profile', views.User_Profile, name="Profile_Page"),
    path('Profile/get-state/',views.get_state,name="get-state"),
    path('Profile/district-json/<str:state>/',views.get_district,name="district-json"),
    path('Profile/ward-pan-json/<str:dist>/',views.get_pan,name="ward-pan-json"),
    path('Profile/ward-ward-json/<str:dist>/',views.get_ward,name="ward-ward-json"),
    path('Logout',views.Logout,name="Logout"),
]