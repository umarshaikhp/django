#crete by umar


from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="BlogHome"),
]




