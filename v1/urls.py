from django.urls import path 
from . import views

app_name="v1"
urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add_product,name='add_product'),
    path('edit/<int:id>/',views.edit_product,name='edit_product'),
    path('delete/<int:id>/',views.delete_product,name='delete_product'),
]