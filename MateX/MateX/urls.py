
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path{'', include(base_pages.urls)}, 
    path('admin/', admin.site.urls),
]
