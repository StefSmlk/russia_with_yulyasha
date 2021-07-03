from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from learning.forms import CommentsImageForm, CommentsVideoForm
from learning.models import BlogVideosModel, BlogImageModel, ImageCommentsModel, VideoCommentsModel


def learning_view_video(request):
    context_video = BlogVideosModel.objects
    comments = VideoCommentsModel.objects
    return render(request, 'learning_video.html', {'video': context_video, 'comments': comments})


def learning_view_photo(request):
    context_photo = BlogImageModel.objects
    comments = ImageCommentsModel.objects
    return render(request, 'learning_photo.html', {'photo': context_photo, 'comments': comments})


def photo_comment_view(request, image_id):
    context_photo = BlogImageModel.objects.get(pk=image_id)
    if request.method == 'POST':
        form = CommentsImageForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.image_id = context_photo.name
            new_form.save()
            return HttpResponseRedirect('/learning/photo')
    else:
        form = CommentsImageForm()
    return render(request, 'comment_photo.html', {'photo': context_photo, 'form': form})
