from django.urls import path
from . import views

app_name = "food"
urlpatterns = [
    # home
    path('', views.index, name='index'),
    # item details
    path('item/<int:item_id>/', views.details, name='details'),
    # add item
    path('add/', views.add_item, name='add_item'),
    # update item
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    # delete item
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]