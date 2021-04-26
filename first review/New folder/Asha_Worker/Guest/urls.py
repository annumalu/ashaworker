from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="GuestHome"),
    path('Login',views.Login,name="Login"),
    path('Registration',views.Register,name="Register"),
    path('Forgot_Password',views.Forgot,name="Forgot"),
]