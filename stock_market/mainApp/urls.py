from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("add", views.add, name="add"), 
    path("edit/<int:id>", views.edit, name="edit"),
    path("listing", views.listing, name="listing"),  
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("<slug:slug>", views.detail, name="detail"),
]