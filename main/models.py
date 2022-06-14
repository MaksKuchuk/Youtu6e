from django.db import models

class Videos(models.Model):
    name = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='images/', null=True)
    video = models.FileField(upload_to='images/', null=True)
    description = models.TextField(blank=True)
    views = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    uploadtime = models.CharField(max_length=20)

    def __str__(self):
        return self.name



