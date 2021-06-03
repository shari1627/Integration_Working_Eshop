from django.db import models

class Categorie(models.Model):
    name=models.CharField(max_length=100) 
    imgtitle=models.CharField(max_length=100)
    imgdesc=models.CharField(max_length=600)
    image=models.ImageField(upload_to="uploads/Images/")
    
    def __str__(self):
        return self.name
        
# @staticmethod
# def get_all_title():
#         return Categorie.objects.all()
# @staticmethod
# def get_title(categoryID):
#         if categoryID:
#               return Categorie.objects.filter(category=categoryID)      
#         else:
#                return  Categorie.objects.all()        