from django.db import models


class ExtractedMusicList(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, default="music")
    musician = models.CharField(max_length=50, default="music singer")
    highlightFile = models.FileField(upload_to='output/')

    def __str__(self):
        return self.title


class MusicStorage(models.Model):
    file = models.FileField(upload_to='music/')
