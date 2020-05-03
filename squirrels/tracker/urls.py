from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('map/', views.sightings_map),
    path('sightings/', views.sightings_list),
    path('sightings/<str:unique_squirrel_id>/', views.get_sighting),
]
