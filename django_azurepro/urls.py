from django.contrib import admin
from django.urls import path
from django_azureapp.views import person_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/', person_list, name='person_list'),
]
