from django.db import models
from django.utils import timezone

# Create your models here.
class musicList(models.Model):
    id = models.IntegerField(primary_key=True)
    created_time = models.DateTimeField(default=timezone.now)
    urls=models.TextField()
    title=models.CharField(max_length=50, default="music")
    start_point=models.IntegerField()
    end_point=models.IntegerField()
