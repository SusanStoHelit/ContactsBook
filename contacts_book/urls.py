from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login_user,name="login"),
    path('logout',views.logout_user,name="logout"),
    path('register',views.register_user,name="register"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('change_password',views.change_password,name="change_password"),
    path('add_contact',views.add_contact,name="add_contact"),
    path('edit/<list_id>',views.edit,name="edit"),
    path('delete/<list_id>',views.delete,name="delete"),
]
