from django.contrib import admin
from .models.post import Post
from .models.lapicero import Lapicero
admin.site.register(Post)
admin.site.register(Lapicero)