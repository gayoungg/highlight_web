from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ExtractedMusicList
from .models import MusicStorage

admin.site.register(ExtractedMusicList)
admin.site.register(MusicStorage)
