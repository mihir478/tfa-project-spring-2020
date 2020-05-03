from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('map/', views.sightings_map),
    path('sighting/',views.sighting_list),
    path('sighting/<str:unique_squirrel_id>/', views.get_sighting),
]
