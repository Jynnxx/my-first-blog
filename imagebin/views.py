from django.shortcuts import render
import os
from .forms import UploadForm
from django.utils import timezone


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
