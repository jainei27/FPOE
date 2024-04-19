from django.contrib import admin
from .models.post import Post
admin.site.register(Post)
from .models.mascota import Mascota
admin.site.register(Mascota)
