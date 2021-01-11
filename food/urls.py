from . import views
from django.urls import path

app_name ='food'
urlpatterns = [
    path('',views.index,name='index'),
    path('item',views.items,name='items'),
    path('<int:item_id>/',views.detail,name='detail'),
    path('add/',views.create_item,name='create_item'),
    path('delete/<int:item_id>/',views.delete_item,name='delete_item'),
    path('edit/<int:item_id>/',views.edit_item,name='edit_item'),
]