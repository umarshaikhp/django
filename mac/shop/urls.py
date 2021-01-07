# crete by umar


from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutAUs"),
    path("contact", views.contact, name="ContactUs"),
    path("tracker", views.tracker, name="TrackingStatus"),
    path("search", views.search, name="Search"),
    # use the <>angle brackets to capture the value from the URL
    path("products/<int:myid>", views.productview, name="ProductView"),
    path("checkout", views.checkout, name="Checkout"),
   
]
