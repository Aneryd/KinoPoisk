from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Film)
admin.site.register(User)
admin.site.register(Serial)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Status)
admin.site.register(FilmGenre)
