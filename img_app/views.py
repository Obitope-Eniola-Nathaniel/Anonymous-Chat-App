from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post
from .form import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id')

    return render(request, "img_app/index.html", {
        "posts": posts
    })


def model_form_upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('img_app:index')
    else:
        form = PostForm()
    return render(request, 'img_app/model_form_upload.html', {
        'form': form
    })