from django.shortcuts import render

# Create your views here.



from django.core.files.storage import FileSystemStorage
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import os
from PIL import Image
import  numpy as np
model=load_model("Hollybood_update_actore23.h5")
def image_classification(hollywood):
    img=load_img(hollywood,target_size=(150,150))
    img=img_to_array(img)/255
    img=np.expand_dims(img,axis=0)
    img=model.predict(img).round(3)
    print(img)
    img=np.argmax(img)
    if img == 0:
        return 'chris_evans'
    elif img == 1:
        return 'chris_hemsworth'
    elif img == 2:
        return 'mark_ruffalo'
    else:
        return 'robert_downey_jr'






def home(request):
    if request.method=="POST":
        image=request.FILES["image"]
        fs=FileSystemStorage()
        imgg=fs.save(image.name,image)
        imgg=fs.url(imgg)
        test_img='.'+imgg
        pred=image_classification(hollywood=test_img)
        return render(request,'home.html',{"pred":pred,"user_img":imgg})

    return render(request,'home.html')
