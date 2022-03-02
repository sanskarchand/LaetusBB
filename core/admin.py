from django.contrib import admin

from .models import Thread, Post, Forum

admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Post)
