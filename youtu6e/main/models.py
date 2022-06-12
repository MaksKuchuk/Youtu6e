from django.db import models

class Videos(models.Model):
    name = models.CharField(max_length=255)
    #preview = models.ImageField()
    #video = models.FileField()
    description = models.TextField()
    views = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    uploadtime = models.CharField(max_length=20)

    def __str__(self):
        return self.name



