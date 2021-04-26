from django.urls import path
from . import views

urlpatterns = [
    path('',views.StaffHome,name="StaffHome"),
    path('Add_Asha',views.Add_Asha,name="Add_Asha"),
    path('Insurance',views.Insurance,name="Insurance"),
    path('Reports',views.Reports,name="StaffReports"),
    path('Feedback',views.StaffFeedback,name="StaffFeedback"),
    path('Logout',views.Logout,name="Logout"),
    path('Add_Asha/get-pan-json/',views.get_pan_data,name="get-pan-json"),
    path('ward-json/<str:state>/',views.get_json_ward,name="ward-json"),
]