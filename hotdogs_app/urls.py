from django.urls import path
from .views import *


urlpatterns = [
    path('',hotdogs_list,name='hot_dogs_list'),
    path('hotdog/<str:id>',hotdog_detail.as_view(),name='hotdog_detail_url'),
    path('create/',hotdog_create,name='hotdog_create_url'),
    path('update/<str:id>',hotdog_update.as_view(),name='hotdog_update_url'),
    path('<str:id>/delete/',hotdog_delete.as_view(),name='hotdog_delete_url'),

]