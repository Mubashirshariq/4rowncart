from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
   path("",views.index,name="ShopHome"),
   path("about/",views.about,name="AboutUs"),
   path("contact/",views.contact,name="ContactUs"),
   path("tracker/",views.track,name="TrackingStatus"),
   path("search",views.search,name="Search"),
   path("productview",views.prodview,name="Search"),
   path("checkout",views.checkout,name="Checkout"),
]