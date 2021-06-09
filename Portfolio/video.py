from django.db import models

class Video (models.Model):
    video=models.FileField(upload_to="uploads/video/")
    caption=models.TextField()
    Poster=models.ImageField(upload_to="uploads/vide/poster")

    @staticmethod
    def get_all_videos():
        return Video.objects.all()

    @staticmethod
    def get_all_videos_by_id(id):
        if id:
            return Video.objects.filter(id=id)
            
        else:
            return  Video.get_all_videos()      
