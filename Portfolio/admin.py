from django.contrib import admin
from Portfolio.models import gallery
from Portfolio.category import Categorie
from Portfolio.video import Video
class AdminCategorie(admin.ModelAdmin):
    list_display=['name']


class Admingallery(admin.ModelAdmin):
    list_display=['category','image']

class AdminVideo(admin.ModelAdmin):
    list_display=['video','caption']

admin.site.register(gallery,Admingallery)
admin.site.register(Categorie,AdminCategorie)
admin.site.register(Video,AdminVideo)
