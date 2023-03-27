from django.urls import path


from . import views

app_name = 'base_pages'
urlpatterns = [
    path{'', views.index , name= 'index'},
]