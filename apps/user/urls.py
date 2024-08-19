from django.urls import path

from .views import about, home


urlpatterns = [
    path('about/', about, name='about'),
    path('', home, name='home'),
]
