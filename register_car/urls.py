from django.urls import path

from register_car import views


urlpatterns = [
    path('register_car/list', views.list_all, name='list_all_car'),
    path('register_car/create', views.create, name='create_car'),
    path('register_car/update/<int:id>', views.update, name='update_car'),
    path('register_car/delete/<int:id>', views.delete, name='delete_car')
]