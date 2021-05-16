from django.urls import path
from . import views


urlpatterns = [
path('register',views.register,name='register'),
path('login',views.login,name="login"),
path('logout',views.logout,name="logout"),
path('account-recovery',views.recovery,name="recovery"),
path('reset',views.recover,name="recover"),


]