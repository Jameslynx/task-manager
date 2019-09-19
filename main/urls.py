from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('to_do/', views.add_todo, name='add_todo'),
    path('<int:todo_id>/delete', views.delete_todo, name="delete")
]