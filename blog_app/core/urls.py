from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('write/',views.create_blog,name="create"),
    path('<int:blog_id>/show_blog/',views.show_blog,name="show_blog"),
    path('<int:blog_id>/edit/',views.edit_blog, name='edit_blog'),
    path('<int:blog_id>/delete/',views.delete_blog, name='delete_blog'),
    path('register/',views.register, name='register'),
    

] 

