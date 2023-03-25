from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="shop"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracking/",views.track,name="Tracking"),
    path("search/",views.search,name="Search"),
    path("productview/",views.prodview,name="ProductView"),
    path("checkout/",views.checkout,name="Checkout")

]