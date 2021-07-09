from django import forms
from django.forms import Textarea

from learning.models import ImageCommentsModel, VideoCommentsModel, BlogImageModel, BlogVideosModel


class CommentsImageForm(forms.ModelForm):
    nick_name = ImageCommentsModel.nick_name
    image_id = ImageCommentsModel.image_id
    text = ImageCommentsModel.text

    class Meta:
        model = ImageCommentsModel
        fields = ('nick_name', 'text')

        widgets = {
            'text': Textarea(attrs={'rows': 5, 'placeholder': 'comment...'}),
            'nick_name': Textarea(attrs={'rows': 1, 'placeholder': 'Please, enter your name'}),
        }


class CommentsVideoForm(forms.ModelForm):
    nick_name = VideoCommentsModel.nick_name
    video_id = VideoCommentsModel.video_id
    text = VideoCommentsModel.text

    class Meta:
        model = VideoCommentsModel
        fields = ('nick_name', 'text')

        widgets = {
            'text': Textarea(attrs={'rows': 5, 'placeholder': 'comment...'}),
            'nick_name': Textarea(attrs={'rows': 1, 'placeholder': 'Please, enter your name'}),
        }


class AddImageForm(forms.ModelForm):

    class Meta:
        model = BlogImageModel
        fields = ('name', 'image', 'description')


class AddVideoForm(forms.ModelForm):

    class Meta:
        model = BlogVideosModel
        fields = ('name', 'image', 'description')
