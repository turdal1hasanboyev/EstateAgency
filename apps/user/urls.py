from django.urls import path

from apps.user.views import about, home


urlpatterns = [
    path('about/', about, name='about'),
    path('', home, name='home'),
]
