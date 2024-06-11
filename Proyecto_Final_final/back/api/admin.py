from django.contrib import admin
from .models.post import Post
from .models.servicios import Servicios
from .models.cliente import Cliente
admin.site.register(Post)
admin.site.register(Servicios)
admin.site.register(Cliente)
