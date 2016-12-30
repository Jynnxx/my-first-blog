from django.shortcuts import render
import os
from .forms import UploadForm
from django.utils import timezone
from .models import Image


# Create your views here.
def page(request):
    if request.method == 'POST':
        img = UploadForm(request.POST, request.FILES)
        if img.is_valid():
            post = img.save(commit=False)
            post.user = request.user
            post.created_date = timezone.now()
            extension = post.file.name.split('.')[-1]
            post.file.name = post.name + '.' + extension
            post.save()

    else:

        img = UploadForm(request.POST or None)
    return render(request, 'imagebin/page.html',{'form':img})

def show(request):
    url = request.path
    file = url[url.find('media/') + 6:]
    files = Image.objects.filter(name = file)
    if files != []:
        return render(request, 'imagebin/found.html', {'image' : files[0]})
    else:
        return render(request, 'imagebin/notfound.html', {})
