from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="GuestHome"),
    path('Login',views.Login,name="Login"),
    path('Donate',views.Donate,name="Donate"),
    path('pdf_view/', views.GeneratePdf.as_view(), name="pdf_view"),
    path('Registration',views.Register,name="Register"),
    path('Forgot_Password',views.Forgot,name="Forgot"),
]