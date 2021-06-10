from django.shortcuts import render
from Portfolio.models import gallery
from Portfolio.category import Categorie
from Portfolio.video import Video


def index(request):
    # image=gallery.get_all_photos()
    # photo=gallery.objects.get(id=pk)
    title=Categorie.objects.all()
    categoryID=request.GET.get('category')
    if categoryID:
        image=gallery.get_all_photos_by_category_id(categoryID)
        title=Categorie.objects.filter(id=categoryID)  
    else:
        image=gallery.get_all_photos() 
        title=Categorie.objects.all()  
    data={}
    data ['image']=image
    data ['title']=title       
     
    return render(request,'image.html', data)
    
    
    
    

def imagedisplay1(request):
    resultdisplay1=Categorie.objects.all()
    
    
    return render(request,'main.html',{'Categorie':resultdisplay1})
    
def video(request):
    
    
    scroll=Video.get_all_videos() 
    id=request.GET.get('id')
    if id:
        video=Video.get_all_videos_by_id(id)
          
    else:
        video=Video.get_all_videos() 
    data={}
    data ['video']=video
    data ['scroll']=scroll        

          
    return render(request,'video.html',data)

  
def home(request):
    return render(request,'home.html')  