from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mubeen/', admin.site.urls),
    path('', include('Blogs.urls'))
]
