from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('discworld/', admin.site.urls),
    path('', include('contacts_book.urls')),
]
