from .  import views
from django.urls import path, include





urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name="logout"),
    path('first_page',views.first_page,name='first_page'),


]