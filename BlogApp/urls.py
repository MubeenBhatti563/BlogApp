from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
=======
    path('mubeen/', admin.site.urls),
>>>>>>> b27d5a5 (Update project with new features)
    path('', include('Blogs.urls'))
]
