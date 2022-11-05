from django.contrib import admin

# Register your models here

from .models import (Song,Artiste,Lyric)

admin.site.register(Song)
admin.site.register(Artiste)
admin.site.register(Lyric)
