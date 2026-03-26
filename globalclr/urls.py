from django.contrib import admin
from django.urls import path
from main.views import home, about, trainers, contact

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('trainers/', trainers, name='trainers'),
    path('contact/', contact, name='contact'),
]