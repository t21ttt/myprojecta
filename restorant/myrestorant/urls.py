from django.urls import path
from.import views




urlpatterns = [
   
     path('', views.new1,name="new1"),
     path('register',views.register,name="register"),
     path('login',views.login,name='login')
]