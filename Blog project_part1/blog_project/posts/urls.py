from django.urls import path
from .import views
urlpatterns = [
    path('add/', views.add_post, name= 'add_post'),
    path('edit/<int:id>',views.edit_post, name= "edit_post"),
    path('delet/<int:id>', views.delet_post,name= 'delet_post')
]