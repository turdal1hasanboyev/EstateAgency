from django.urls import path

from apps.property.views import property, property_single


urlpatterns = [
    path("property/", property, name="property"),
    path("property-single/<slug:slug>/", property_single, name="property-single")
]
