from django import forms
from django.forms import Textarea

from learning.models import ImageCommentsModel, VideoCommentsModel, BlogImageModel, BlogVideosModel


class CommentsImageForm(forms.ModelForm):
    image_id = ImageCommentsModel.image_id
    text = ImageCommentsModel.text

    class Meta:
        model = ImageCommentsModel
        fields = ('text',)

        widgets = {
            'text': Textarea(attrs={'rows': 5, 'cols': 60}),
        }


class CommentsVideoForm(forms.ModelForm):
    video_id = VideoCommentsModel.video_id
    text = VideoCommentsModel.text

    class Meta:
        model = VideoCommentsModel
        fields = ('text',)

        widgets = {
            'text': Textarea(attrs={'rows': 5, 'cols': 60}),
        }


class AddImageForm(forms.ModelForm):

    class Meta:
        model = BlogImageModel
        fields = ('name', 'image', 'description')


class AddVideoForm(forms.ModelForm):

    class Meta:
        model = BlogVideosModel
        fields = ('name', 'image', 'description')
