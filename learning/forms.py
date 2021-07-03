from django import forms

from learning.models import ImageCommentsModel, VideoCommentsModel, BlogImageModel


class CommentsImageForm(forms.ModelForm):
    image_id = ImageCommentsModel.image_id
    text = ImageCommentsModel.text

    class Meta:
        model = ImageCommentsModel
        fields = ('text',)


class CommentsVideoForm(forms.ModelForm):
    video_id = VideoCommentsModel.video_id
    text = VideoCommentsModel.text

    class Meta:
        model = VideoCommentsModel
        fields = ('text',)
