from django.urls import path
from . import views

#이거 있어야 리다이렉트 편하게 하는듯
app_name = 'todolist'
urlpatterns = [
    path('',views.index,name='index'),
    path('write/',views.write,name='write'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),

]
