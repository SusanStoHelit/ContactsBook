from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add_contact',views.add_contact,name="add_contact"),
    path('edit/<list_id>',views.edit,name="edit"),
    path('delete/<list_id>',views.delete,name="delete"),
]
