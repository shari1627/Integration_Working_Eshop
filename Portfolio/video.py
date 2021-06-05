from django.db import models

class Video (models.Model):
    video=models.FileField(upload_to="uploads/video/")
    caption=models.TextField()
    Poster=models.ImageField(upload_to="uploads/vide/poster")