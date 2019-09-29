from django.shortcuts import render, redirect
from .models import Post
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import auth
from PIL import Image
import os
from celery import shared_task
from .task import resize_file

# login contains login funcationality
def login(request):
    if request.user.id=='':
        return HttpResponseRedirect('/upload')

    if request.method=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/post')
        else:
            return redirect('/login')				
    return render(request, 'registration/login.html')

# logout functionailty
def logout(request):
	auth.logout(request)
	return redirect('/login')

# Upload image
@login_required(login_url='/login/')
def upload(request):
    try:
        if request.method == 'POST' and request.FILES['image']:
            myfile = request.FILES['image']
            ps = Post(author_id=request.user.id,image=myfile)
            ps.save()
            psObj = Post.objects.get(pk=ps.id)

            sourceimage = settings.MEDIA_ROOT +'/'+psObj.image.name
            name, extension = os.path.splitext(psObj.image.name)
            newfilename = str(psObj.id)+extension

            resize_file.delay(sourceimage, settings.MEDIA_ROOT +'/vs_image/'+newfilename, (100,100))
            resize_file.delay(sourceimage, settings.MEDIA_ROOT +'/small_image/'+newfilename, (200,200))
            resize_file.delay(sourceimage, settings.MEDIA_ROOT +'/bl_image/'+newfilename, (300,300))

            return render(request, 'post.html')
        return render(request, 'post.html')
    except Exception as e:
        print (e)

# list image of login user
@login_required(login_url='/login/')
def image_list(request):
    try:
        data = Post.objects.filter(author_id=request.user.id)
        return render(request,"post_list.html", {'data': data})

    except Exception as e:
        print (e)


# list image of login user
@login_required(login_url='/login/')
def sub_image_list(request,id):
    try:
        if int(id)>0:
            psObj = Post.objects.get(pk=id)
            name, extension = os.path.splitext(psObj.image.name)
            newfilename = str(psObj.id)+extension

            return render(request,"post_sublist.html", {'image_name': newfilename,'media_url':settings.MEDIA_URL})

    except Exception as e:
        print (e)



