from django.contrib import admin
from .models import Blog
<<<<<<< HEAD

# Register your models here.
admin.site.register(Blog)
=======
from .models import Comment

# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)
>>>>>>> b27d5a5 (Update project with new features)
